from Monitor_Metric import Monitor_Metric
from Monitor_MetricDAO import Monitor_Metric


class SQLMonitor_Monitor_Metric(Monitor_Metric):

    def __init__(self, conn):
        self.conn = conn

    def get_all_monitor_metric(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Monitor_Metric")
        rows = cursor.fetchall()
        monitor_metrics = []
        for row in rows:
            monitor_metric = Monitor_Metric(row[0], row[1])
            monitor_metrics.append(monitor_metric)
        return monitor_metrics

    def insert_monitor_metric(self, monitor_device_id, metric_id):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Monitor_Metric VALUES (?, ?)",(monitor_device_id, metric_id))
        self.conn.commit()

    def update_monitor_metric(self, monitor_metric):
        cursor = self.conn.cursor()
        sql = "UPDATE Monitor_Metric SET "
        params = []

        if monitor_metric.metric_id:
            sql += "metric_id  = %s, "
            params.append(monitor_metric.metric_id)

        # Remove the trailing comma and space
        sql = sql.rstrip(", ")

        sql += " WHERE monitor_device_id  = %s"
        params.append(monitor_metric.monitor_device_id)
        cursor.execute(sql, tuple(params))
        self.conn.commit()

    def delete_monitor_metric(self, metric_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Monitor_Metric WHERE metric_id = ?",metric_id)
        self.conn.commit()

    def search_monitor_metric(self, monitor_device_id):
        cursor = self.conn.cursor()
        sql = "SELECT * FROM Monitor_Metric WHERE monitor_device_id = %s "
        cursor.execute(sql, (monitor_device_id,))
        rows = cursor.fetchall()
        monitor_metrics = []
        for row in rows:
            monitor_metric = Monitor_Metric(row[0], row[1])
            monitor_metrics.append(monitor_metric)
        return monitor_metrics

    def query_average_metric_count(self):
        cursor = self.conn.cursor()
        sql = "SELECT AVG(metric_count) AS avg_metric_count " \
              "FROM (" \
              "SELECT m.device_name, COUNT(DISTINCT met.metric_id) AS metric_count " \
              "FROM Monitor_Metric mm " \
              "JOIN Monitor m ON mm.monitor_device_id = m.device_id " \
              "JOIN Metric met ON mm.metric_id = met.metric_id " \
              "GROUP BY m.device_name " \
              ") AS subquery"
        cursor.execute(sql)
        row = cursor.fetchone()
        avg_metric_count = row[0]
        return avg_metric_count

    def query_max_metric_count(self):
        cursor = self.conn.cursor()
        sql = "SELECT MAX(metric_count) AS max_metric_count " \
              "FROM (" \
              "SELECT m.device_name, COUNT(DISTINCT met.metric_id) AS metric_count " \
              "FROM Monitor_Metric mm " \
              "JOIN Monitor m ON mm.monitor_device_id = m.device_id " \
              "JOIN Metric met ON mm.metric_id = met.metric_id " \
              "GROUP BY m.device_name " \
              ") AS subquery"
        cursor.execute(sql)
        row = cursor.fetchone()
        max_metric_count = row[0]
        return max_metric_count

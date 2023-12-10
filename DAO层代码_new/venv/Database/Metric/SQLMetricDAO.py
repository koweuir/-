from Metric import Metric
from MetricDAO import MetricDAO


class SQLMetricDAO(MetricDAO):
    def __init__(self, conn):
        self.conn = conn

    def get_all_metric(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Metric")
        rows = cursor.fetchall()
        metrics = []
        for row in rows:
            metric = Metric(row[0], row[1])
            metrics.append(metric)
        return metrics

    def insert_metric(self, metric_name):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Metric VALUES (?)", metric_name)
        self.conn.commit()

    def update_metric(self, metric):
        cursor = self.conn.cursor()
        sql = "UPDATE Metric SET "
        params = []

        if metric.metric_name:
            sql += "metric_name  = %s, "
            params.append(metric.metric_name)

        # Remove the trailing comma and space
        sql = sql.rstrip(", ")

        sql += " WHERE metric_id  = %s"
        params.append(metric.metric_id)
        cursor.execute(sql, tuple(params))
        self.conn.commit()

    def delete_metric(self, metric_id):
        cursor = self.conn.cursor()
        sql = "DELETE FROM Metric WHERE metric_id = ?",
        cursor.execute(sql, (metric_id,))
        self.conn.commit()

    def search_metric(self, metric_id):
        cursor = self.conn.cursor()
        sql = "SELECT * FROM Metric WHERE metric_id = %s "
        cursor.execute(sql, (metric_id,))
        rows = cursor.fetchall()
        metrics = []
        for row in rows:
            metric = Metric(row[0], row[1])
            metrics.append(metric)
        return metrics

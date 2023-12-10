from Monitoring import Monitoring
from MonitoringDAO import MonitoringDAO


class SQLMonitoringDAO(MonitoringDAO):
    def __init__(self, conn):
        self.conn = conn

    def get_all_monitoring(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Monitoring")
        rows = cursor.fetchall()
        monitors = []
        for row in rows:
            monitor = Monitoring(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            monitors.append(monitor)
        return monitors

    def insert_monitoring(self, monitoring):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Monitoring VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       (monitoring.monitoring_time, monitoring.monitor_person, monitoring.monitoring_location,
                        monitoring.target_plant_id, monitoring.monitoring_index, monitoring.creator,
                        monitoring.create_time, monitoring.update_time)
                       )
        self.conn.commit()

    def update_monitoring(self, monitoring):
        cursor = self.conn.cursor()
        sql = "UPDATE Monitoring SET "
        params = []

        if monitoring.monitoring_time:
            sql += "monitoring_time = %s, "
            params.append(monitoring.monitoring_time)

        if monitoring.monitor_person:
            sql += "monitor_person = %s, "
            params.append(monitoring.monitor_person)

        if monitoring.monitoring_location:
            sql += "monitoring_location = %s, "
            params.append(monitoring.monitoring_location)

        if monitoring.target_plant_id:
            sql += "target_plant_id = %s, "
            params.append(monitoring.target_plant_id)

        if monitoring.monitoring_index:
            sql += "monitoring_index = %s, "
            params.append(monitoring.monitoring_index)

        if monitoring.update_time:
            sql += "update_time = %s, "
            params.append(monitoring.update_time)

        # Remove the trailing comma and space
        sql = sql.rstrip(", ")

        sql += " WHERE monitoring_id = %s"
        params.append(monitoring.monitoring_id)

        cursor.execute(sql, tuple(params))
        self.conn.commit()

    def delete_monitoring(self, monitoring_id):
        cursor = self.conn.cursor()
        sql = "DELETE FROM Monitoring WHERE monitoring_id = ?",
        cursor.execute(sql, (monitoring_id,))
        self.conn.commit()

    def search_monitoring(self, monitoring):
        cursor = self.conn.cursor()
        sql = "SELECT * FROM Monitoring WHERE 1 = 1 "
        params = []
        if monitoring.monitoring_time:
            sql += "AND monitoring_time like concat('%',%s,'%') "
            params.append(monitoring.monitoring_time)
        if monitoring.monitor_person:
            sql += "OR monitor_person like concat('%',%s,'%') "
            params.append(monitoring.monitor_person)
        if monitoring.monitoring_location:
            sql += "OR monitoring_location like concat('%',%s,'%') "
            params.append(monitoring.monitoring_location)
        if monitoring.target_plant_id:
            sql += "OR target_plant_id = %s "
            params.append(monitoring.target_plant_id)
        if monitoring.monitoring_index:
            sql += "OR monitoring_index = %s "
            params.append(monitoring.monitoring_index)
        cursor.execute(sql, tuple(params))
        rows = cursor.fetchall()
        monitoring_list = []
        for row in rows:
            monitoring = Monitoring(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            monitoring_list.append(monitoring)
        return monitoring_list

    def query_monitor_plants(self, monitor_device_id):
        cursor = self.conn.cursor()
        sql = "SELECT m.device_name, p.plant_id, p.alias AS plant_name " \
              "FROM Monitor_Plants mp " \
              "JOIN Monitor m ON mp.monitor_device_id = m.device_id " \
              "JOIN Plants p ON mp.plant_id = p.plant_id " \
              "WHERE m.device_id = ?"
        cursor.execute(sql, (monitor_device_id,))
        rows = cursor.fetchall()
        monitor_plants = []
        for row in rows:
            monitor_plant = {
                'device_name': row[0],
                'plant_id': row[1],
                'plant_name': row[2]
            }
            monitor_plants.append(monitor_plant)
        return monitor_plants

    def query_device_metric_count(self, monitor_device_id):
        cursor = self.conn.cursor()
        sql = "SELECT m.device_name, COUNT(DISTINCT met.metric_id) AS metric_count " \
              "FROM Monitor_Metric mm " \
              "JOIN Monitor m ON mm.monitor_device_id = m.device_id " \
              "JOIN Metric met ON mm.metric_id = met.metric_id " \
              "WHERE m.device_id = ? " \
              "GROUP BY m.device_name"
        cursor.execute(sql, (monitor_device_id,))
        rows = cursor.fetchall()
        device_metric_counts = []
        for row in rows:
            device_metric_count = {
                'device_name': row[0],
                'metric_count': row[1]
            }
            device_metric_counts.append(device_metric_count)
        return device_metric_counts

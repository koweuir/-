from Monitoring import Monitoring
from MonitoringDAO import MonitoringDAO


class SQLMonitoringDAO(MonitoringDAO):
    def __init__(self, conn):
        self.conn = conn

    def get_all_monitoring(self):
        cursor = self.conn.cursor()
        cursor.execute("")
        rows = cursor.fetchall()
        monitors = []
        for row in rows:
            monitor = Monitoring(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            monitors.append(monitor)
        return monitors

    def create_monitoring(self, monitoring):
        cursor = self.conn.cursor()
        sql = "INSERT INTO Monitoring VALUES (%d, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (monitoring.monitoring_id, monitoring.monitoring_time, monitoring.monitor_person, monitoring.monitoring_location,
                  monitoring.target_plant_id, monitoring.monitoring_index, monitoring.monitoring_device,
                  monitoring.creator, monitoring.create_time, monitoring.update_time)
        cursor.execute(sql, values)
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

        if monitoring.monitoring_device:
            sql += "monitoring_device = %s, "
            params.append(monitoring.monitoring_device)

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
        sql = "DELETE FROM Monitoring WHERE monitoring_id = %s"
        cursor.execute(sql, (monitoring_id,))
        self.conn.commit()

    def search_monitoring(self, monitoring):
        cursor = self.conn.cursor()
        sql = "SELECT * FROM Monitoring WHERE 1=1 "
        params = []

        if monitoring.monitoring_time:
            sql += "AND monitoring_time LIKE CONCAT('%', %s, '%') "
            params.append(monitoring.monitoring_time)

        if monitoring.monitor_person:
            sql += "AND monitor_person LIKE CONCAT('%', %s, '%') "
            params.append(monitoring.monitor_person)

        if monitoring.monitoring_location:
            sql += "AND monitoring_location LIKE CONCAT('%', %s, '%') "
            params.append(monitoring.monitoring_location)

        if monitoring.target_plant_id:
            sql += "AND target_plant_id = %d "
            params.append(monitoring.target_plant_id)

        if monitoring.monitoring_index:
            sql += "AND monitoring_index = %d "
            params.append(monitoring.monitoring_index)

        if monitoring.monitoring_device:
            sql += "AND monitoring_device LIKE CONCAT('%', %s, '%') "
            params.append(monitoring.monitoring_device)

        cursor.execute(sql, tuple(params))
        rows = cursor.fetchall()
        monitorings = []
        for row in rows:
            monitoring = Monitoring(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            monitorings.append(monitoring)
        return monitorings

    def get_average_monitoring_index(self, target_plant_id):
        cursor = self.conn.cursor()
        sql = "SELECT AVG(monitoring_index) AS average_index " \
              "FROM Monitoring " \
              "WHERE target_plant_id = %s"

        cursor.execute(sql, (target_plant_id,))
        row = cursor.fetchone()
        average_index = row[0] if row[0] is not None else 0  # 处理结果为 None 的情况
        return average_index

    def get_max_monitoring_index(self, target_plant_id):
        cursor = self.conn.cursor()
        sql = "SELECT MAX(monitoring_index) AS max_index " \
              "FROM Monitoring " \
              "WHERE target_plant_id = %s"

        cursor.execute(sql, (target_plant_id,))
        row = cursor.fetchone()
        max_index = row[0] if row[0] is not None else 0  # 处理结果为 None 的情况
        return max_index

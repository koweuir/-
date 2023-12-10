from Monitor import Monitor
from MonitorDAO import MonitorDAO


class SQLMonitorDAO(MonitorDAO):
    def __init__(self, conn):
        self.conn = conn

    def get_all_monitor(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Monitor")
        rows = cursor.fetchall()
        monitors = []
        for row in rows:
            monitor = Monitor(row[0], row[1])
            monitors.append(monitor)
        return monitors

    def insert_monitor(self, device_name):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Monitor VALUES (?)", device_name)
        self.conn.commit()

    def update_monitor(self, monitor):
        cursor = self.conn.cursor()
        sql = "UPDATE Monitor SET "
        params = []

        if monitor.device_name:
            sql += "device_name = %s, "
            params.append(monitor.device_name)

        # Remove the trailing comma and space
        sql = sql.rstrip(", ")

        sql += " WHERE device_id = %s"
        params.append(monitor.device_id)
        cursor.execute(sql, tuple(params))
        self.conn.commit()

    def delete_monitor(self, device_id):
        cursor = self.conn.cursor()
        sql = "DELETE FROM Monitor WHERE device_id = ?",
        cursor.execute(sql, (device_id,))
        self.conn.commit()

    def search_monitor(self, device_id):
        cursor = self.conn.cursor()
        sql = "SELECT * FROM Monitor WHERE device_id = %s "
        cursor.execute(sql, (device_id,))
        rows = cursor.fetchall()
        monitors = []
        for row in rows:
            monitor = Monitor(row[0], row[1])
            monitors.append(monitor)
        return monitors

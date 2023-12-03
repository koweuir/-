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

    def create_monitoring(self, monitor):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO 课程表 (课程号, 课程名, 学分数, 学时数, 任课教师) VALUES (?, ?, ?, ?, ?)",
                       (monitor.monitoring_id, monitor.monitoring_time, monitor.monitor_person,
                        monitor.monitoring_location, monitor.target_plant_id, monitor.monitoring_index,
                        monitor.monitoring_device, monitor.creator, monitor.create_time, monitor.update_time))
        self.conn.commit()

from Monitor_Plants import Monitor_Plants
from Monitor_PlantsDAO import Monitor_PlantsDAO


class SQLMonitor_PlantsDAO(Monitor_PlantsDAO):
    def __init__(self, conn):
        self.conn = conn

    def get_monitor_device_id(self, plant_id):
        cursor = self.conn.cursor()
        sql = "SELECT monitor_device_id FROM Monitor_Plants WHERE plant_id = %s"
        cursor.execute(sql, (plant_id,))
        row = cursor.fetchone()
        if row:
            return row[0]
        else:
            return None

    def get_plant_id(self, monitor_device_id):
        cursor = self.conn.cursor()
        sql = "SELECT plant_id FROM Monitor_Plants WHERE monitor_device_id = %s"
        cursor.execute(sql, (monitor_device_id,))
        row = cursor.fetchone()
        if row:
            return row[0]
        else:
            return None

    def insert_monitor_plants(self, monitor_device_id, plant_id):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Monitor_Plants VALUES (?, ?)", (monitor_device_id, plant_id))
        self.conn.commit()

    def update_monitor_plants(self, metric_id, plant_id):
        cursor = self.conn.cursor()
        sql = "UPDATE Monitor_Plants SET plant_id = %s WHERE monitor_device_id = (SELECT monitor_device_id FROM Monitor_Metric WHERE metric_id = %s)"
        params = [plant_id, metric_id]
        cursor.execute(sql, tuple(params))
        self.conn.commit()

    def delete_monitor_plants(self, monitoring_id):
        cursor = self.conn.cursor()
        cursor.execute(
            "DELETE FROM Monitor_Plants WHERE plant_id = (SELECT target_plant_id FROM Monitoring WHERE monitoring_id = ?)",
            monitoring_id)
        self.conn.commit()

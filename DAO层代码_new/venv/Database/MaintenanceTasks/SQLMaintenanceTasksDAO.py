from MaintenanceTasks import MaintenanceTasks
from MaintenanceTasksDAO import MaintenanceTasksDAO


class SQLMaintenanceTasksDAO(MaintenanceTasksDAO):
    def __init__(self, conn):
        self.conn = conn

    def get_all_maintenanceTasks(self):
        cursor = self.conn.cursor()
        cursor.execute("select * from MaintenanceTasks")
        rows = cursor.fetchall()
        tasks = []
        for row in rows:
            task = MaintenanceTasks(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            tasks.append(task)
        return tasks

    def insert_maintenanceTasks(self, maintenanceTasks):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO MaintenanceTasks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (
                           maintenanceTasks.task_name, maintenanceTasks.execution_time,
                           maintenanceTasks.execution_location,
                           maintenanceTasks.executor, maintenanceTasks.task_description,
                           maintenanceTasks.target_plant_id,
                           maintenanceTasks.creator, maintenanceTasks.create_time, maintenanceTasks.update_time)
                       )
        self.conn.commit()

    def delete_task(self, task_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM MaintenanceTasks WHERE task_id = ?", (task_id,))
        self.conn.commit()

    def update_task(self, maintenanceTasks):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE MaintenanceTasks SET task_name = ?, execution_time = ?, execution_location = ?, executor = ?, task_description = ?, target_plant_id = ?, update_time = ? WHERE task_id = ?",
            (maintenanceTasks.task_id, maintenanceTasks.task_name, maintenanceTasks.execution_time,
             maintenanceTasks.execution_location, maintenanceTasks.executor, maintenanceTasks.task_description,
             maintenanceTasks.target_plant_id, maintenanceTasks.update_time)
        )
        self.conn.commit()

    def search_tasks(self, maintenanceTasks):
        cursor = self.conn.cursor()
        sql = "SELECT * FROM MaintenanceTasks WHERE task_name like concat('%',?,'%') OR execution_time like concat('%',?,'%') OR execution_location like concat('%',?,'%') OR executor like concat('%',?,'%') OR task_description like concat('%',?,'%') OR target_plant_id like concat('%',?,'%')"
        params = (maintenanceTasks.task_name, maintenanceTasks.execution_time, maintenanceTasks.execution_location,
                  maintenanceTasks.executor, maintenanceTasks.task_description, maintenanceTasks.target_plant_id)
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        tasks = []
        for row in rows:
            task = MaintenanceTasks(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            tasks.append(task)
        return tasks

    def search_maintenance_task_plant_info(self, task_id):
        cursor = self.conn.cursor()
        sql = "SELECT MT.task_name AS MaintenanceTaskName,P.alias AS PlantAlias,P.disease_name AS PlantDiseaseName,M.monitoring_index AS MonitoringIndex " \
              "FROM MaintenanceTasks MT " \
              "JOIN Plants P ON MT.target_plant_id = P.plant_id " \
              "LEFT JOIN Monitoring M ON P.plant_id = M.target_plant_id " \
              "WHERE MT.task_id = %s"
        cursor.execute(sql, (task_id,))
        rows = cursor.fetchall()
        plant_info = []
        for row in rows:
            info = {
                'MaintenanceTaskName': row[0],
                'PlantAlias': row[1],
                'PlantDiseaseName': row[2],
                'MonitoringIndex': row[3]
            }
            plant_info.append(info)
        return plant_info

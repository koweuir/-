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

    def create_maintenanceTasks(self, maintenanceTasks):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO MaintenanceTasks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (
                           maintenanceTasks.task_name, maintenanceTasks.execution_time,
                           maintenanceTasks.execution_location,
                           maintenanceTasks.executor, maintenanceTasks.task_description,
                           maintenanceTasks.target_plant_id,
                           maintenanceTasks.creator, maintenanceTasks.create_time, maintenanceTasks.update_time))
        self.conn.commit()

    def delete_task(self, task_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM MaintenanceTasks WHERE task_id = ?", (task_id,))
        self.conn.commit()

    def update_task(self, taskname, executiontime, exelocal, executor, describe, targetid, updatetime, taskid):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE MaintenanceTasks SET task_name = ?, execution_time = ?, execution_location = ?, executor = ?, task_description = ?, target_plant_id = ?, update_time = ? WHERE task_id = ?",
            (taskname, executiontime, exelocal, executor, describe, targetid, updatetime, taskid))

        self.conn.commit()

    def search_tasks(self, info):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM MaintenanceTasks WHERE task_name like concat('%%',?,'%%') OR execution_time like concat('%%',?,'%%') OR execution_location like concat('%%',?,'%%') OR executor like concat('%%',?,'%%') OR task_description like concat('%%',?,'%%') OR target_plant_id like concat('%%',?,'%%')",
            (info, info, info, info, info, info,))
        rows = cursor.fetchall()
        '''tasks = []
        for row in rows:
            task = MaintenanceTasks(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            tasks.append(task)'''
        return rows

    def search_plant_monitoring_maintenance(self, task_id):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT MT.task_name AS MaintenanceTaskName,P.alias AS PlantAlias,P.disease_name AS PlantDiseaseName,M.monitoring_index AS MonitoringIndex FROM MaintenanceTasks MT "
            "JOIN Plants P ON MT.target_plant_id = P.plant_id "
            "LEFT JOIN Monitoring M ON P.plant_id = M.target_plant_id "
            "WHERE MT.task_id = ?", (task_id,))
        '''rows = cursor.fetchall()
        result=[]
        for row in rows:
            re = MaintenanceTasks(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            result.append(re)'''
        return cursor.fetchall()

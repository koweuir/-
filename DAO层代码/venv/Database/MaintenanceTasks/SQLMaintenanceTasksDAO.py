from MaintenanceTasks import MaintenanceTasks
from MaintenanceTasksDAO import MaintenanceTasksDAO


class SQLMaintenanceTasksDAO(MaintenanceTasksDAO):
    def __init__(self, conn):
        self.conn = conn

    def get_all_maintenanceTasks(self):
        cursor = self.conn.cursor()
        cursor.execute("")
        rows = cursor.fetchall()
        tasks = []
        for row in rows:
            task = MaintenanceTasks(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            tasks.append(task)
        return tasks

    def create_maintenanceTasks(self, task):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO 课程表 (课程号, 课程名, 学分数, 学时数, 任课教师) VALUES (?, ?, ?, ?, ?)",
                       (task.task_id, task.task_name, task.execution_time, task.execution_location, task.executor, task.task_description, task.target_plant_id, task.create_time, task.update_time))
        self.conn.commit()

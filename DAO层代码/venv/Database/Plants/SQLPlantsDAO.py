from Plants import Plants
from PlantsDAO import PlantsDAO
class SQLPlantsDAO(PlantsDAO):
    def __init__(self, conn):
        self.conn = conn

    def get_all_plants(self):
        cursor = self.conn.cursor()
        cursor.execute("")
        rows = cursor.fetchall()
        plants = []
        for row in rows:
            plant = Plants(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            plants.append(plant)
        return plants

    def create_plants(self, plant):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO 课程表 (课程号, 课程名, 学分数, 学时数, 任课教师) VALUES (?, ?, ?, ?, ?)",
                       (plant.plant_id, plant.species_id, plant.disease_name, plant.alias, plant.morphology, plant.cultivation_techniques, plant.utilization_value, plant.creator, plant.create_time, plant.update_time))
        self.conn.commit()

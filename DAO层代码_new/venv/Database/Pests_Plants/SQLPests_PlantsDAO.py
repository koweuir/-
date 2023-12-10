from Pests_Plants import Pests_Plants
from Pests_PlantsDAO import Pests_PlantsDAO


class SQLPests_PlantsDAO(Pests_PlantsDAO):
    def __init__(self, conn):
        self.conn = conn

    def getPestByPlant(self, plant_id):
        cursor = self.conn.cursor()
        sql = "SELECT pest_id FROM Pests_Plants WHERE plant_id = %s"
        cursor.execute(sql, (plant_id,))
        row = cursor.fetchone()
        if row:
            return row[0]
        else:
            return None

    def getPlantByPest(self, pest_id):
        cursor = self.conn.cursor()
        sql = "SELECT plant_id FROM Pests_Plants WHERE pest_id = %s"
        cursor.execute(sql, (pest_id,))
        row = cursor.fetchone()
        if row:
            return row[0]
        else:
            return None

    def insert(self, pest_id, plant_id):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Pests_Plants VALUES (?, ?)", (pest_id, plant_id))
        self.conn.commit()

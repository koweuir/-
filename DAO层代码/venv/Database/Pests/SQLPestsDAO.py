from Pests import Pests
from PestsDAO import PestsDAO


class SQLPestsDAO(PestsDAO):
    def __init__(self, conn):
        self.conn = conn

    def get_all_pests(self):
        cursor = self.conn.cursor()
        cursor.execute("")
        rows = cursor.fetchall()
        pests = []
        for row in rows:
            pest = Pests(row[0], row[1], row[2], row[3], row[4])
            pests.append(pest)
        return pests

    def create_pests(self, pest):
        cursor = self.conn.cursor()
        sql = "INSERT INTO Pests VALUES (%d, %s, %s, %s, %s)"
        params = (pest.pest_id, pest.pest_name, pest.creator, pest.create_time, pest.update_time)

        cursor.execute(sql, params)
        self.conn.commit()

    def update_pests(self, pest):
        cursor = self.conn.cursor()
        sql = "UPDATE Pests SET "
        params = []

        if pest.pest_name:
            sql += "pest_name = %s, "
            params.append(pest.pest_name)

        if pest.update_time:
            sql += "update_time = %s, "
            params.append(pest.update_time)

        # Remove the trailing comma and space from the SQL statement
        sql = sql[:-2]

        sql += " WHERE pest_id = %s"
        params.append(pest.pest_id)

        cursor.execute(sql, tuple(params))
        self.conn.commit()

    def search_pests(self, pest_name=None):
        cursor = self.conn.cursor()
        sql = "SELECT * FROM Pests WHERE 1 = 1 "
        params = []

        if pest_name:
            sql += "AND pest_name like concat('%',%s,'%') "
            params.append(pest_name)

        cursor.execute(sql, tuple(params))
        rows = cursor.fetchall()
        pests = []
        for row in rows:
            pest = Pests(row[0], row[1], row[2], row[3], row[4])
            pests.append(pest)
        return pests

    def delete_pest(self, pest_id):
        cursor = self.conn.cursor()
        sql = "DELETE FROM Pests WHERE pest_id = %s"
        cursor.execute(sql, (pest_id,))
        self.conn.commit()

    def search_pest_control_strategies(self, plant_id):
        cursor = self.conn.cursor()
        sql = "SELECT P.pest_name,PCS.method,PCS.pesticide_name,PCS.pesticide_amount,PCS.effective_period,PCS.other_info FROM Plants PL "
        sql += "JOIN PestControlStrategies PCS ON PCS.plant_id = PL.plant_id "
        sql += "JOIN Pests P ON P.pest_id = PCS.pest_id "
        sql += "WHERE PL.plant_id = %s"
        cursor.execute(sql, (plant_id,))
        rows = cursor.fetchall()
        pest_control_strategies = []
        for row in rows:
            pest_control_strategy = {
                'pest_name': row[0],
                'method': row[1],
                'pesticide_name': row[2],
                'pesticide_amount': row[3],
                'effective_period': row[4],
                'other_info': row[5]
            }
            pest_control_strategies.append(pest_control_strategy)
        return pest_control_strategies

    def search_family_by_disease(self, disease_name):
        cursor = self.conn.cursor()
        sql = "SELECT f.family_name FROM Families f "
        sql += "INNER JOIN Genera g ON f.family_id = g.family_id "
        sql += "INNER JOIN Species s ON g.genus_id = s.genus_id "
        sql += "INNER JOIN Plants p ON s.species_id = p.species_id "
        sql += "WHERE p.disease_name = %s"
        cursor.execute(sql, (disease_name,))
        rows = cursor.fetchall()
        families = []
        for row in rows:
            family = row[0]
            families.append(family)
        return families

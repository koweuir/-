from Pests import Pests
from PestsDAO import PestsDAO


class SQLPestsDAO(PestsDAO):
    def __init__(self, conn):
        self.conn = conn

    def get_all_pests(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Pests WHERE 1 = 1")
        rows = cursor.fetchall()
        pests = []
        for row in rows:
            pest = Pests(row[0], row[1], row[2], row[3], row[4])
            pests.append(pest)
        return pests

    def insert_pests(self, pests):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Pests VALUES (?, ?, ?, ?)",
                       (pests.pest_name, pests.creator, pests.create_time, pests.update_time))
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

    def search_pest_control(self, plant_id):
        cursor = self.conn.cursor()
        sql = "SELECT P.pest_name,PCS.method,PCS.pesticide_name,PCS.pesticide_amount,PCS.effective_period,PCS.other_info FROM Plants PL " \
              "JOIN PestControlStrategies PCS ON PCS.plant_id = PL.plant_id " \
              "JOIN Pests P ON P.pest_id = PCS.pest_id " \
              "WHERE PL.plant_id = %s"
        cursor.execute(sql, (plant_id,))
        rows = cursor.fetchall()
        pest_controls = []
        for row in rows:
            pest_control = {
                'pest_name': row[0],
                'method': row[1],
                'pesticide_name': row[2],
                'pesticide_amount': row[3],
                'effective_period': row[4],
                'other_info': row[5]
            }
            pest_controls.append(pest_control)
        return pest_controls

    def search_family_by_pest(self, pest_name):
        cursor = self.conn.cursor()
        sql = "SELECT DISTINCT F.family_name " \
              "FROM Families F " \
              "INNER JOIN Genera G ON F.family_id = G.family_id " \
              "INNER JOIN Species S ON G.genus_id = S.genus_id " \
              "INNER JOIN Plants P ON S.species_id = P.species_id " \
              "INNER JOIN Pests_Plants PP ON P.plant_id = PP.plant_id " \
              "INNER JOIN Pests PT ON PP.pest_id = PT.pest_id " \
              "WHERE PT.pest_name = %s"
        cursor.execute(sql, (pest_name,))
        rows = cursor.fetchall()
        families = [row[0] for row in rows]
        return families

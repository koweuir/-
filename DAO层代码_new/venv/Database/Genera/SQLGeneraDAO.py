from Genera import Genera
from GeneraDAO import GeneraDAO


class SQLGeneraDAO(GeneraDAO):
    def __init__(self, conn):
        self.conn = conn

    def get_all_genera(self):
        cursor = self.conn.cursor()
        cursor.execute("select * from from Genera")
        rows = cursor.fetchall()
        generals = []
        for row in rows:
            genera = Genera(row[0], row[1], row[2], row[3], row[4])
            generals.append(genera)
        return generals

    def insert_genus(self, genera):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Genera VALUES (?, ?, ?, ?, ?)",
                       (genera.family_id, genera.genus_name, genera.creator, genera.create_time, genera.update_time))
        self.conn.commit()

    def delete_genus(self, genus_name):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Genera WHERE genus_name = ?", genus_name)
        self.conn.commit()

    def update_genus(self, genera):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE Genera SET family_id = ?, genus_name = ?, update_time = ? WHERE genus_id = ?",
                       (genera.genus_id, genera.family_id, genera.genus_name, genera.update_time))
        self.conn.commit()

    def search_genera(self, genus_id, genus_name):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Genera WHERE genus_id = ? OR  genus_name like concat('%',?,'%')", (genus_id, genus_name))
        rows = cursor.fetchall()
        genera = []
        for row in rows:
            genus = Genera(row[0], row[1], row[2], row[3], row[4], row[5])
            genera.append(genus)
        return genera

    def delete_genera_by_family(self, family_name):
        cursor = self.conn.cursor()
        sql = "DELETE FROM Genera WHERE family_id = " \
              "(SELECT family_id FROM Families WHERE family_name = ?)"
        cursor.execute(sql, (family_name,))
        self.conn.commit()

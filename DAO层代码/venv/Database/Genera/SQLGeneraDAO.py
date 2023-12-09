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

    def create_genus(self, genus):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Genera VALUES (?,?,?,?,?)",
                       (genus.family_id, genus.genus_name, genus.creator, genus.create_time, genus.update_time))
        self.conn.commit()

    def delete_genus(self, genus_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Genera WHERE genus_id = ?", (genus_id,))
        self.conn.commit()

    def update_genus(self, genusName, genusUpdateTime, genusId):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE Genera SET genus_name = ?, update_time = ? WHERE genus_id = ?",
                       (genusName, genusUpdateTime, genusId))
        self.conn.commit()

    def search_genera(self, genus_name):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Genera WHERE genus_name like concat('%%', ?, '%%')", (genus_name,))
        rows = cursor.fetchall()
        genera = []
        for row in rows:
            genus = Genera(row[0], row[1], row[2], row[3], row[4], row[5])
            genera.append(genus)
        return genera

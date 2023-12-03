from Genera import Genera
from GeneraDAO import GeneraDAO


class SQLGeneraDAO(GeneraDAO):
    def __init__(self, conn):
        self.conn = conn

    def get_all_genera(self):
        cursor = self.conn.cursor()
        cursor.execute("")
        rows = cursor.fetchall()
        generals = []
        for row in rows:
            genera = Genera(row[0], row[1], row[2], row[3], row[4])
            generals.append(genera)
        return generals

    def create_genera(self, genera):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO 课程表 (课程号, 课程名, 学分数, 学时数, 任课教师) VALUES (?, ?, ?, ?, ?)",
                       (genera.genus_id, genera.family_id, genera.genus_name, genera.creator, genera.create_time, genera.update_time))
        self.conn.commit()

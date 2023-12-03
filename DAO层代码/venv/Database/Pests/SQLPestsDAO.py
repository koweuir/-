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
        cursor.execute("INSERT INTO 课程表 (课程号, 课程名, 学分数, 学时数, 任课教师) VALUES (?, ?, ?, ?, ?)",
                       (pest.pest_id, pest.pest_name, pest.creator, pest.create_time, pest.update_time))
        self.conn.commit()

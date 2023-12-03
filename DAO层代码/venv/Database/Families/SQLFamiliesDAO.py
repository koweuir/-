from Families import Families
from FamiliesDAO import FamiliesDAO


class SQLFamiliesDAO(FamiliesDAO):
    def __init__(self, conn):
        self.conn = conn

    def get_all_families(self):
        cursor = self.conn.cursor()
        cursor.execute("")
        rows = cursor.fetchall()
        families = []
        for row in rows:
            family = Families(row[0], row[1], row[2], row[3], row[4])
            families.append(family)
        return families

    def create_families(self, family):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO 课程表 (课程号, 课程名, 学分数, 学时数, 任课教师) VALUES (?, ?, ?, ?, ?)",
                       (family.family_id, family.family_name, family.creator, family.create_time, family.update_time))
        self.conn.commit()

from Pictures import Pictures
from PicturesDAO import PicturesDAO
class SQLPicturesDAO(PicturesDAO):
    def __init__(self, conn):
        self.conn = conn

    def get_all_pictures(self):
        cursor = self.conn.cursor()
        cursor.execute("")
        rows = cursor.fetchall()
        pictures = []
        for row in rows:
            picture = Pictures(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            pictures.append(picture)
        return pictures

    def create_pictures(self, picture):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO 课程表 (课程号, 课程名, 学分数, 学时数, 任课教师) VALUES (?, ?, ?, ?, ?)",
                       (picture.picture_id, picture.plant_id, picture.position, picture.descrip, picture.photographer, picture.creator, picture.create_time, picture.update_time))
        self.conn.commit()

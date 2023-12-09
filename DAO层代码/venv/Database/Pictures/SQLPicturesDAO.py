from Pictures import Pictures
from PicturesDAO import PicturesDAO


class SQLPicturesDAO(PicturesDAO):
    def __init__(self, conn):
        self.conn = conn

    def create_pictures(self, picture):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO Pictures (picture_id, plant_id, position, descrip, photographer, creator, create_time, update_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (picture.picture_id, picture.plant_id, picture.position, picture.descrip, picture.photographer,
             picture.creator, picture.create_time, picture.update_time))
        self.conn.commit()

    def get_all_picturesById(self, plant_id):
        cursor = self.conn.cursor()
        sql = "SELECT * FROM Pictures WHERE plant_id = %s"
        cursor.execute(sql, (plant_id,))
        rows = cursor.fetchall()
        pictures = []
        for row in rows:
            picture = Pictures(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            pictures.append(picture)
        return pictures

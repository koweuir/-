from Species import Species
from SpeciesDAO import SpeciesDAO
class SQLSpeciesDAO(SpeciesDAO):
    def __init__(self, conn):
        self.conn = conn

    def get_all_species(self):
        cursor = self.conn.cursor()
        cursor.execute("")
        rows = cursor.fetchall()
        species = []
        for row in rows:
            specie = Species(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            species.append(specie)
        return species

    def create_species(self, specie):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO 课程表 (课程号, 课程名, 学分数, 学时数, 任课教师) VALUES (?, ?, ?, ?, ?)",
                       (specie.species_id, specie.genus_id, specie.species_name, specie.region, specie.env, specie.creator, specie.create_time, specie.update_time))
        self.conn.commit()

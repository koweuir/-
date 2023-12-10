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
            specie = Species(row[0], row[1], row[2], row[3], row[4], row[5])
            species.append(specie)
        return species

    def insert_species(self, species):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO Species VALUES (?, ?, ?, ?, ?)",
                       (species.genus_id, species.species_name, species.creator, species.create_time, species.update_time))
        self.conn.commit()

    def delete_species_by_name(self, species_name):
        cursor = self.conn.cursor()
        sql = "DELETE FROM Species WHERE species_name = ?"
        cursor.execute(sql, (species_name,))
        self.conn.commit()

    def update_species(self, species):
        cursor = self.conn.cursor()
        sql = "UPDATE Species SET "
        update_fields = []
        params = []

        if species.genus_id is not None:
            update_fields.append("genus_id = %s")
            params.append(species.genus_id)
        if species.species_name is not None:
            update_fields.append("species_name = %s")
            params.append(species.species_name)
        if species.update_time is not None:
            update_fields.append("update_time = %s")
            params.append(species.update_time)

        # 检查是否有需要更新的字段
        if len(update_fields) == 0:
            return  # 如果没有需要更新的字段，则直接返回

        sql += ", ".join(update_fields)
        sql += " WHERE species_id = %s"
        params.append(species.species_id)

        cursor.execute(sql, tuple(params))
        self.conn.commit()

    def search_species(self, species_id=None, species_name=None):
        cursor = self.conn.cursor()
        sql = "SELECT * FROM Species WHERE 1 = 1 "
        params = []
        if species_id:
            sql += "AND species_id = ? "
            params.append(species_id)
        if species_name:
            sql += "OR species_name like concat('%',?,'%') "
            params.append(species_name)
        cursor.execute(sql, tuple(params))
        rows = cursor.fetchall()
        species_list = []
        for row in rows:
            species = Species(row[0], row[1], row[2], row[3], row[4])
            species_list.append(species)
        return species_list

    def delete_species_by_family(self, family_name):
        cursor = self.conn.cursor()
        sql = "DELETE FROM Species WHERE genus_id IN " \
              "(SELECT genus_id FROM Genera WHERE family_id = " \
              "(SELECT family_id FROM Families WHERE family_name = ?))"
        cursor.execute(sql, (family_name,))
        self.conn.commit()

    def delete_species_by_genus(self, genus_name):
        cursor = self.conn.cursor()
        sql = "DELETE FROM Species WHERE genus_id = " \
              "(SELECT genus_id FROM Genera WHERE genus_name = ?)"
        cursor.execute(sql, (genus_name,))
        self.conn.commit()


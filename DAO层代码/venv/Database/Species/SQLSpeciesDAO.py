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
            specie = Species(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            species.append(specie)
        return species

    def create_species(self, specie):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO Species (species_id, genus_id, species_name, region, env, creator, create_time, update_time) VALUES (%d ,%s, %s, %s, %s, %s, %s, %s)",
            (specie.species_id, specie.genus_id, specie.species_name, specie.region, specie.env, specie.creator, specie.create_time,
             specie.update_time))
        self.conn.commit()

    def delete_species_by_id(self, species_id):
        cursor = self.conn.cursor()
        sql = "DELETE FROM Species WHERE species_id = %s"
        cursor.execute(sql, (species_id,))
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
        if species.region is not None:
            update_fields.append("region = %s")
            params.append(species.region)
        if species.env is not None:
            update_fields.append("env = %s")
            params.append(species.env)
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

    def search_species(self, species):
        cursor = self.conn.cursor()
        sql = "SELECT * FROM Species WHERE 1 = 1 "
        params = []

        if species.species_name:
            sql += "AND species_name like concat('%',%s,'%') "
            params.append(species.species_name)

        if species.region:
            sql += "AND region like concat('%',%s,'%') "
            params.append(species.region)

        if species.env:
            sql += "AND env like concat('%',%s,'%') "
            params.append(species.env)

        cursor.execute(sql, tuple(params))
        result = cursor.fetchall()
        return result

    def search_species_by_env(self, env):
        cursor = self.conn.cursor()
        sql = "SELECT * FROM Species WHERE env like concat('%',%s,'%')"
        params = (env,)

        cursor.execute(sql, params)
        rows = cursor.fetchall()
        species_list = []
        for row in rows:
            species = Species(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            species_list.append(species)
        return species_list


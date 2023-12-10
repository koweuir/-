from Plants import Plants
from PlantsDAO import PlantsDAO


class SQLPlantsDAO(PlantsDAO):

    def __init__(self, conn):
        self.conn = conn

    def get_all_plants(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Plants")
        rows = cursor.fetchall()
        plants = []
        for row in rows:
            plant = Plants(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                           row[11], row[12])
            plants.append(plant)
        return plants

    def insert_plants(self, plant):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Plants VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?)",
                       (plant.species_id, plant.alias, plant.morphology, plant.province, plant.city, plant.county,
                        plant.growth_environment, plant.cultivation_techniques, plant.utilization_value, plant.creator,
                        plant.create_time, plant.update_time)
                       )
        cursor.execute("INSERT INTO Pests_Plants VALUES(?, ?)",
                       (plant.pest_id, plant.plant_id))
        self.conn.commit()

    def delete_plant_by_id(self, plant_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Plants WHERE plant_id = ?", plant_id)
        self.conn.commit()

    def update_plant(self, plant):
        cursor = self.conn.cursor()
        sql = "UPDATE Plants SET "
        update_fields = []
        params = []
        if plant.alias:
            update_fields.append("species_id = %s")
            params.append(plant.species_id)
        if plant.alias:
            update_fields.append("alias = %s")
            params.append(plant.alias)
        if plant.morphology:
            update_fields.append("morphology = %s")
            params.append(plant.morphology)
        if plant.province:
            update_fields.append("province = %s")
            params.append(plant.province)
        if plant.city:
            update_fields.append("city = %s")
            params.append(plant.city)
        if plant.county:
            update_fields.append("county = %s")
            params.append(plant.county)
        if plant.growth_environment:
            update_fields.append("growth_environment  = %s")
            params.append(plant.growth_environment)
        if plant.cultivation_techniques:
            update_fields.append("cultivation_techniques = %s")
            params.append(plant.cultivation_techniques)
        if plant.utilization_value:
            update_fields.append("utilization_value = %s")
            params.append(plant.utilization_value)
        if plant.update_time:
            update_fields.append("update_time = %s")
            params.append(plant.update_time)

        sql += ", ".join(update_fields)
        sql += " WHERE plant_id = %s"
        params.append(plant.plant_id)

        cursor.execute(sql, tuple(params))
        self.conn.commit()

    def search_plants(self, plant_id=None, alias=None, morphology=None, province=None, city=None, county=None,
                      growth_environment=None, cultivation_techniques=None, utilization_value=None):
        cursor = self.conn.cursor()
        sql = "SELECT * FROM Plants WHERE 1 = 1 "
        params = []
        if plant_id:
            sql += "AND plant_id = %s "
            params.append(plant_id)
        if alias:
            sql += "AND alias LIKE concat('%',%s,'%') "
            params.append(alias)
        if morphology:
            sql += "AND morphology LIKE concat('%',%s,'%') "
            params.append(morphology)
        if province:
            sql += "AND province LIKE concat('%',%s,'%') "
            params.append(province)
        if city:
            sql += "AND city LIKE concat('%',%s,'%') "
            params.append(city)
        if county:
            sql += "AND county LIKE concat('%',%s,'%') "
            params.append(county)
        if growth_environment:
            sql += "AND growth_environment LIKE concat('%',%s,'%') "
            params.append(growth_environment)
        if cultivation_techniques:
            sql += "AND cultivation_techniques LIKE concat('%',%s,'%') "
            params.append(cultivation_techniques)
        if utilization_value:
            sql += "AND utilization_value LIKE concat('%',%s,'%') "
            params.append(utilization_value)

        cursor.execute(sql, tuple(params))
        rows = cursor.fetchall()
        plants = []
        for row in rows:
            # Assuming the Plant class has a constructor that takes all these parameters:
            plant = Plants(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                           row[10], row[11], row[12])
            plants.append(plant)
        return plants

    def search_plant_species_info(self, plant_id):
        cursor = self.conn.cursor()
        sql = "SELECT sp.species_name, gn.genus_name, fm.family_name FROM Plants pl " \
              "INNER JOIN Species sp ON pl.species_id = sp.species_id " \
              "INNER JOIN Genera gn ON sp.genus_id = gn.genus_id " \
              "INNER JOIN Families fm ON gn.family_id = fm.family_id " \
              "WHERE pl.plant_id = ?"
        cursor.execute(sql, (plant_id,))
        rows = cursor.fetchall()
        plant_species_info = []
        for row in rows:
            species_name = row[0]
            genus_name = row[1]
            family_name = row[2]
            plant_species_info.append((species_name, genus_name, family_name))
        return plant_species_info

    def search_sub_plants(self, species_name):
        cursor = self.conn.cursor()
        sql = "SELECT * FROM Plants " \
              "JOIN Species ON Plants.species_id = Species.species_id " \
              "WHERE species_name like concat('%',?,'%')"
        cursor.execute(sql, (species_name,))
        rows = cursor.fetchall()
        plants = []
        for row in rows:
            plant = Plants(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                           row[11], row[12])
            plants.append(plant)
        return plants

    def search_plants_by_growth_environment(self, plant):
        cursor = self.conn.cursor()
        sql = "SELECT * FROM Plants WHERE province like concat('%',?,'%') OR city like concat('%',?,'%') OR county like concat('%',?,'%') OR growth_environment like concat('%',?,'%')"
        params = (plant.province, plant.city, plant.county, plant.growth_environment)
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        plants = []
        for row in rows:
            plant = Plants(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                           row[11], row[12])
            plants.append(plant)
        return plants

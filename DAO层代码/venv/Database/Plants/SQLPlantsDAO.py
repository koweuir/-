from Plants import Plants
from PlantsDAO import PlantsDAO


class SQLPlantsDAO(PlantsDAO):
    def __init__(self, conn):
        self.conn = conn

    def get_all_plants(self):
        cursor = self.conn.cursor()
        cursor.execute("")
        rows = cursor.fetchall()
        plants = []
        for row in rows:
            plant = Plants(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            plants.append(plant)
        return plants

    def create_plants(self, plant):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Plants VALUES (%d, %d, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (plant.plant_id, plant.species_id, plant.disease_name, plant.alias, plant.morphology,
                        plant.cultivation_techniques, plant.utilization_value, plant.creator, plant.create_time,
                        plant.update_time))
        self.conn.commit()

    def delete_plant_by_id(self, plant_id):
        cursor = self.conn.cursor()
        sql = "DELETE FROM Plants WHERE plant_id = %s"
        cursor.execute(sql, (plant_id,))
        self.conn.commit()

    def update_plant(self, plant):
        cursor = self.conn.cursor()
        sql = "UPDATE Plants SET "
        update_fields = []
        params = []
        if plant.disease_name:
            update_fields.append("disease_name = %s")
            params.append(plant.disease_name)
        if plant.alias:
            update_fields.append("alias = %s")
            params.append(plant.alias)
        if plant.morphology:
            update_fields.append("morphology = %s")
            params.append(plant.morphology)
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

    def search_plants(self, disease_name=None, alias=None, morphology=None, cultivation_techniques=None,
                      utilization_value=None):
        cursor = self.conn.cursor()
        sql = "SELECT * FROM Plants WHERE 1 = 1 "
        params = []

        if disease_name:
            sql += "AND disease_name like concat('%',%s,'%') "
            params.append(disease_name)

        if alias:
            sql += "AND alias like concat('%',%s,'%') "
            params.append(alias)

        if morphology:
            sql += "AND morphology like concat('%',%s,'%') "
            params.append(morphology)

        if cultivation_techniques:
            sql += "AND cultivation_techniques like concat('%',%s,'%') "
            params.append(cultivation_techniques)

        if utilization_value:
            sql += "AND utilization_value like concat('%',%s,'%') "
            params.append(utilization_value)

        cursor.execute(sql, tuple(params))
        rows = cursor.fetchall()
        plants = []
        for row in rows:
            plant = Plants(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            plants.append(plant)
        return plants

    def get_plant_information(self, plant_id):
        cursor = self.conn.cursor()
        sql = "SELECT sp.species_name, gn.genus_name, fm.family_name FROM Plants pl " \
              "INNER JOIN Species sp ON pl.species_id = sp.species_id " \
              "INNER JOIN Genera gn ON sp.genus_id = gn.genus_id " \
              "INNER JOIN Families fm ON gn.family_id = fm.family_id " \
              "WHERE pl.plant_id = %s"
        cursor.execute(sql, (plant_id,))
        result = cursor.fetchone()
        return result

    def search_subordinate_plants(self, species_name=None, region=None, env=None):
        cursor = self.conn.cursor()
        sql = "SELECT * FROM Plants JOIN Species ON Plants.species_id = Species.species_id WHERE 1=1 "

        params = []
        if species_name:
            sql += "AND species_name like concat('%',%s,'%') "
            params.append(species_name)

        if region:
            sql += "AND region like concat('%',%s,'%') "
            params.append(region)

        if env:
            sql += "AND env like concat('%',%s,'%') "
            params.append(env)

        cursor.execute(sql, tuple(params))
        rows = cursor.fetchall()
        plants = []
        for row in rows:
            plant = Plants(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            plants.append(plant)
        return plants

from Families import Families
from FamiliesDAO import FamiliesDAO


class SQLFamiliesDAO(FamiliesDAO):
    def __init__(self, conn):
        self.conn = conn

    def get_all_families(self):
        cursor = self.conn.cursor()
        cursor.execute("select * from Families")
        rows = cursor.fetchall()
        families = []
        for row in rows:
            family = Families(row[0], row[1], row[2], row[3], row[4])
            families.append(family)
        return families

    def create_families(self, family):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Families VALUES (?, ?, ?, ?)",
                       (family.family_name, family.creator, family.create_time, family.update_time))
        self.conn.commit()

    def delete_family(self, family_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Families WHERE family_id = ?", (family_id,))
        self.conn.commit()

    def update_family(self, familyName, familyUpdateTime, familyId):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE Families SET family_name = ?, update_time = ? WHERE family_id = ?",
                       (familyName, familyUpdateTime, familyId))
        self.conn.commit()

    def search_family(self, family_name):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Families WHERE family_name like concat('%%', ?, '%%')", (family_name,))
        rows = cursor.fetchall()
        families = []
        for row in rows:
            family = Families(row[0], row[1], row[2], row[3], row[4])
            families.append(family)
        return families

    def count_plants_by_family(self):
        cursor = self.conn.cursor()

        sql = (
            "SELECT Families.family_name, COUNT(Plants.plant_id) AS plant_count "
            "FROM Families "
            "LEFT JOIN Genera ON Families.family_id = Genera.family_id "
            "LEFT JOIN Species ON Genera.genus_id = Species.genus_id "
            "LEFT JOIN Plants ON Species.species_id = Plants.species_id "
            "GROUP BY Families.family_name "
            "ORDER BY plant_count DESC"
        )
        cursor.execute(sql)
        rows = cursor.fetchall()
        family_counts = []
        for row in rows:
            family_name = row[0]
            plant_count = row[1]
            family_counts.append((family_name, plant_count))
        return family_counts
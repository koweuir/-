from PestControlStrategies import PestControlStrategies
from PestControlStrategiesDAO import PestControlStrategiesDAO
class SQLPestControlStrategiesDAO(PestControlStrategiesDAO):
    def __init__(self, conn):
        self.conn = conn

    def insert_pestControlStrategies(self, strategy):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO PestControlStrategies VALUES (%d, %d, %s, %s, %s, %s, %s)",
                       (strategy.strategy_id, strategy.pest_id, strategy.method, strategy.pesticide_name, strategy.pesticide_amount, strategy.effective_period, strategy.other_info))
        self.conn.commit()

    def search_pest_control_strategies(self, plant_id):
        cursor = self.conn.cursor()
        sql = "SELECT * FROM PestControlStrategies WHERE pest_id = (SELECT pest_id FROM Pests_Plants WHERE plant_id = ?)"
        cursor.execute(sql, (plant_id,))
        rows = cursor.fetchall()
        strategies = []
        for row in rows:
            strategy = PestControlStrategies(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            strategies.append(strategy)
        return strategies


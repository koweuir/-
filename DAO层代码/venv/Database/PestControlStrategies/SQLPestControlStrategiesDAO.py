from PestControlStrategies import PestControlStrategies
from PestControlStrategiesDAO import PestControlStrategiesDAO
class SQLPestControlStrategiesDAO(PestControlStrategiesDAO):
    def __init__(self, conn):
        self.conn = conn

    def get_all_pestControlStrategies(self):
        cursor = self.conn.cursor()
        cursor.execute("")
        rows = cursor.fetchall()
        strategies = []
        for row in rows:
            strategy = PestControlStrategies(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            strategies.append(strategy)
        return strategies

    def create_pestControlStrategies(self, strategy):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO 课程表 (课程号, 课程名, 学分数, 学时数, 任课教师) VALUES (?, ?, ?, ?, ?)",
                       (strategy.strategy_id, strategy.pest_id, strategy.method, strategy.pesticide_name, strategy.pesticide_amount, strategy.effective_period, strategy.other_info))
        self.conn.commit()

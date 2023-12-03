from AbnormalMonitoringRecords import AbnormalMonitoringRecords
from AbnormalMonitoringRecordsDAO import AbnormalMonitoringRecordsDAO


class SQLAbnormalMonitoringRecordsDAO(AbnormalMonitoringRecordsDAO):
    def __init__(self, conn):
        self.conn = conn

    def get_all_abnormalMonitoringRecords(self):
        cursor = self.conn.cursor()
        cursor.execute("")
        rows = cursor.fetchall()
        records = []
        for row in rows:
            Record = AbnormalMonitoringRecords(row[0], row[1], row[2], row[3], row[4])
            records.append(Record)
        return records

    def create_abnormalMonitoringRecords(self, record):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO 课程表 (课程号, 课程名, 学分数, 学时数, 任课教师) VALUES (?, ?, ?, ?, ?)",
                       (record.record_id, record.monitoring_id, record.abnormal_value, record.record_time, record.remark))
        self.conn.commit()

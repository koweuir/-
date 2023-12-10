from AbnormalMonitoringRecords import AbnormalMonitoringRecords
from AbnormalMonitoringRecordsDAO import AbnormalMonitoringRecordsDAO


class SQLAbnormalMonitoringRecordsDAO(AbnormalMonitoringRecordsDAO):
    def __init__(self, conn):
        self.conn = conn

    def get_all_abnormalMonitoringRecords(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM AbnormalMonitoringRecords")
        rows = cursor.fetchall()
        records = []
        for row in rows:
            Record = AbnormalMonitoringRecords(row[0], row[1], row[2], row[3], row[4])
            records.append(Record)
        return records

    def insert_abnormalMonitoringRecords(self, record):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO AbnormalMonitoringRecords VALUES (?, ?, ?, ?, ?)",
                       (record.record_id, record.monitoring_id, record.abnormal_value, record.record_time, record.remark))
        self.conn.commit()

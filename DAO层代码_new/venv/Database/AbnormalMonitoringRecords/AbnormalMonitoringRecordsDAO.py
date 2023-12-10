from abc import ABC, abstractmethod


class AbnormalMonitoringRecordsDAO(ABC):
    @abstractmethod
    def get_all_abnormalMonitoringRecords(self):
        pass

    @abstractmethod
    def insert_abnormalMonitoringRecords(self, record):
        pass

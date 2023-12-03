from abc import ABC, abstractmethod


class MonitoringDAO(ABC):
    @abstractmethod
    def get_all_monitoring(self):
        pass

    @abstractmethod
    def create_monitoring(self, monitor):
        pass

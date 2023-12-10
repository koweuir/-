from abc import ABC, abstractmethod


class MonitoringDAO(ABC):
    @abstractmethod
    def get_all_monitoring(self):
        pass

    @abstractmethod
    def insert_monitoring(self, monitor):
        pass

    @abstractmethod
    def update_monitoring(self, monitoring):
        pass

    @abstractmethod
    def delete_monitoring(self, monitoring_id):
        pass

    @abstractmethod
    def search_monitoring(self, monitoring):
        pass

    @abstractmethod
    def query_monitor_plants(self, monitor_device_id):
        pass

    @abstractmethod
    def query_device_metric_count(self, monitor_device_id):
        pass


from abc import ABC, abstractmethod


class Monitor_Metric(ABC):
    @abstractmethod
    def get_all_monitor_metric(self):
        pass

    @abstractmethod
    def get_monitor_device_id(self, metric_id):
        pass

    @abstractmethod
    def get_metric_id(self, monitor_device_id):
        pass

    @abstractmethod
    def insert_monitor_metric(self, monitor_device_id, metric_id):
        pass

    @abstractmethod
    def update_monitor_metric(self, monitor_metric):
        pass

    @abstractmethod
    def delete_monitor_metric(self, metric_id):
        pass

    @abstractmethod
    def search_monitor_metric(self, monitor_device_id):
        pass

    @abstractmethod
    def query_average_metric_count(self):
        pass

    @abstractmethod
    def query_max_metric_count(self):
        pass




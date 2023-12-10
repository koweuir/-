from abc import ABC, abstractmethod


class MetricDAO(ABC):
    @abstractmethod
    def get_all_metric(self):
        pass

    @abstractmethod
    def insert_metric(self, metric_name):
        pass

    @abstractmethod
    def update_metric(self, monitor):
        pass

    @abstractmethod
    def delete_metric(self, device_id):
        pass

    @abstractmethod
    def search_metric(self, device_id):
        pass

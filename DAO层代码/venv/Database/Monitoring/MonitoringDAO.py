from abc import ABC, abstractmethod


class MonitoringDAO(ABC):
    @abstractmethod
    def get_all_monitoring(self):
        pass

    @abstractmethod
    def create_monitoring(self, monitor):
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
    def get_average_monitoring_index(self, target_plant_id):
        pass

    @abstractmethod
    def get_max_monitoring_index(self, target_plant_id):
        pass

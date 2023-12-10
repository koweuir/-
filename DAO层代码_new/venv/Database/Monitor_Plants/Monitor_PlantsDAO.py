from abc import ABC, abstractmethod


class Monitor_PlantsDAO(ABC):
    @abstractmethod
    def get_monitor_device_id(self, plant_id):
        pass

    @abstractmethod
    def get_plant_id(self, monitor_device_id):
        pass

    @abstractmethod
    def insert_monitor_plants(self, monitor_device_id, plant_id):
        pass

    @abstractmethod
    def update_monitor_plants(self, metric_id, plant_id):
        pass

    @abstractmethod
    def delete_monitor_plants(self, monitor_device_id):
        pass

from abc import ABC, abstractmethod


class MaintenanceTasksDAO(ABC):
    @abstractmethod
    def get_all_maintenanceTasks(self):
        pass

    @abstractmethod
    def create_maintenanceTasks(self, task):
        pass

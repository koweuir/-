from abc import ABC, abstractmethod


class MaintenanceTasksDAO(ABC):
    @abstractmethod
    def get_all_maintenanceTasks(self):
        pass

    @abstractmethod
    def insert_maintenanceTasks(self, task):
        pass

    @abstractmethod
    def delete_task(self, task_id):
        pass

    @abstractmethod
    def update_task(self, maintenanceTasks):
        pass

    @abstractmethod
    def search_tasks(self, info):
        pass

    @abstractmethod
    def search_maintenance_task_plant_info(self, task_id):
        pass

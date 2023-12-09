from abc import ABC, abstractmethod


class PlantsDAO(ABC):
    @abstractmethod
    def get_all_plants(self):
        pass

    @abstractmethod
    def create_plants(self, plant):
        pass

    @abstractmethod
    def delete_plant_by_id(self, plant_id):
        pass

    @abstractmethod
    def update_plant(self, plant):
        pass

    @abstractmethod
    def search_plants(self, disease_name,alias,morphology,cultivation_techniques,utilization_value):
        pass

    @abstractmethod
    def get_plant_information(self, plant_id):
        pass

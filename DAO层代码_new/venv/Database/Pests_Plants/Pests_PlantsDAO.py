from abc import ABC, abstractmethod


class Pests_PlantsDAO(ABC):
    @abstractmethod
    def getPestByPlant(self, plant_id):
        pass

    @abstractmethod
    def getPlantByPest(self, plant_id):
        pass

    @abstractmethod
    def insert(self, pest_id, plant_id):
        pass



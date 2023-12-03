from abc import ABC, abstractmethod


class PlantsDAO(ABC):
    @abstractmethod
    def get_all_plants(self):
        pass

    @abstractmethod
    def create_plants(self, plant):
        pass

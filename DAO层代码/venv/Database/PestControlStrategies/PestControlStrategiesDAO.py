from abc import ABC, abstractmethod


class PestControlStrategiesDAO(ABC):
    @abstractmethod
    def create_pestControlStrategies(self, strategy):
        pass

    @abstractmethod
    def get_all_pestControlStrategies(self, plant_id):
        pass



from abc import ABC, abstractmethod


class PestControlStrategiesDAO(ABC):
    @abstractmethod
    def insert_pestControlStrategies(self, strategy):
        pass

    @abstractmethod
    def search_pest_control_strategies(self, plant_id):
        pass



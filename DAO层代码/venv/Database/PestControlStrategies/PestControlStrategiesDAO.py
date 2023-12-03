from abc import ABC, abstractmethod


class PestControlStrategiesDAO(ABC):
    @abstractmethod
    def get_all_pestControlStrategies(self):
        pass

    @abstractmethod
    def create_pestControlStrategies(self, strategy):
        pass

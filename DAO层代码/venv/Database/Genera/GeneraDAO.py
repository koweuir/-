from abc import ABC, abstractmethod


class GeneraDAO(ABC):
    @abstractmethod
    def get_all_genera(self):
        pass

    @abstractmethod
    def create_genus(self, genera):
        pass

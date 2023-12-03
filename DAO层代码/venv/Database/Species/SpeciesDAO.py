from abc import ABC, abstractmethod


class SpeciesDAO(ABC):
    @abstractmethod
    def get_all_species(self):
        pass

    @abstractmethod
    def create_species(self, specie):
        pass

from abc import ABC, abstractmethod


class SpeciesDAO(ABC):
    @abstractmethod
    def get_all_species(self):
        pass

    @abstractmethod
    def create_species(self, specie):
        pass

    @abstractmethod
    def delete_species_by_id(self, species_id):
        pass

    @abstractmethod
    def update_species(self, species):
        pass

    @abstractmethod
    def search_species(self, species):
        pass

    @abstractmethod
    def search_species_by_env(self, env):
        pass

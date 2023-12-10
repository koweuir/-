from abc import ABC, abstractmethod


class SpeciesDAO(ABC):
    @abstractmethod
    def get_all_species(self):
        pass

    @abstractmethod
    def insert_species(self, species):
        pass

    @abstractmethod
    def delete_species_by_name(self, species_id):
        pass

    @abstractmethod
    def update_species(self, species):
        pass

    @abstractmethod
    def search_species(self, species_id, species_name):
        pass

    @abstractmethod
    def delete_species_by_family(self, family_name):
        pass

    @abstractmethod
    def delete_species_by_genus(self, genus_name):
        pass

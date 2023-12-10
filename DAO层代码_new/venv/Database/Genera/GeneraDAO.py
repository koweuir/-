from abc import ABC, abstractmethod


class GeneraDAO(ABC):
    @abstractmethod
    def get_all_genera(self):
        pass

    @abstractmethod
    def insert_genus(self, genera):
        pass

    @abstractmethod
    def delete_genus(self, genus_id):
        pass

    @abstractmethod
    def update_genus(self, genera):
        pass

    @abstractmethod
    def search_genera(self, genus_id, genus_name):
        pass

    @abstractmethod
    def delete_genera_by_family(self, family_name):
        pass

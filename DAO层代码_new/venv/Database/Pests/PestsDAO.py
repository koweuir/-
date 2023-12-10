from abc import ABC, abstractmethod


class PestsDAO(ABC):
    @abstractmethod
    def get_all_pests(self):
        pass

    @abstractmethod
    def insert_pests(self, pest):
        pass

    @abstractmethod
    def update_pests(self, pests):
        pass

    @abstractmethod
    def delete_pest(self, pest_id):
        pass

    @abstractmethod
    def search_pests(self, pest_name=None):
        pass

    @abstractmethod
    def search_pest_control(self, plant_id):
        pass

    @abstractmethod
    def search_family_by_pest(self, pest_name):
        pass



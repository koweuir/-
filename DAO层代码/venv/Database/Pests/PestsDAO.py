from abc import ABC, abstractmethod


class PestsDAO(ABC):
    @abstractmethod
    def get_all_pests(self):
        pass

    @abstractmethod
    def create_pests(self, pest):
        pass

    @abstractmethod
    def update_pests(self, pest):
        pass

    @abstractmethod
    def delete_pest(self, pest_id):
        pass

    @abstractmethod
    def search_pest_control_strategies(self, plant_id):
        pass

    @abstractmethod
    def search_family_by_disease(self, disease_name):
        pass

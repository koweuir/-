from abc import ABC, abstractmethod


class FamiliesDAO(ABC):
    @abstractmethod
    def get_all_families(self):
        pass

    @abstractmethod
    def insert_families(self, family):
        pass

    @abstractmethod
    def delete_family(self, family_id):
        pass

    @abstractmethod
    def update_family(self, familyName, familyUpdateTime, familyId):
        pass

    @abstractmethod
    def search_family(self, family_id, family_name):
        pass

    @abstractmethod
    def count_plants_by_family(self):
        pass

from abc import ABC, abstractmethod


class FamiliesDAO(ABC):
    @abstractmethod
    def get_all_families(self):
        pass

    @abstractmethod
    def create_families(self, family):
        pass

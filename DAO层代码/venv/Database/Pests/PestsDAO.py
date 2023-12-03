from abc import ABC, abstractmethod


class PestsDAO(ABC):
    @abstractmethod
    def get_all_pests(self):
        pass

    @abstractmethod
    def create_pests(self, pest):
        pass

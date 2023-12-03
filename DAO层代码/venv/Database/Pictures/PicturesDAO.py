from abc import ABC, abstractmethod


class PicturesDAO(ABC):
    @abstractmethod
    def get_all_pictures(self):
        pass

    @abstractmethod
    def create_pictures(self, picture):
        pass

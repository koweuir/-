from abc import ABC, abstractmethod


class PicturesDAO(ABC):

    @abstractmethod
    def create_pictures(self, picture):
        pass

    @abstractmethod
    def search_pictures(self, plant_id):
        pass


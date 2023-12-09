from abc import ABC, abstractmethod


class PicturesDAO(ABC):
    @abstractmethod
    def get_all_picturesById(self, plant_id):
        pass

    @abstractmethod
    def create_pictures(self, picture):
        pass

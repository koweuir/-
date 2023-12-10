from abc import ABC, abstractmethod


class MonitorDAO(ABC):
    @abstractmethod
    def get_all_monitor(self):
        pass

    @abstractmethod
    def insert_monitor(self, monitor):
        pass

    @abstractmethod
    def update_monitor(self, monitor):
        pass

    @abstractmethod
    def delete_monitor(self, device_id):
        pass

    @abstractmethod
    def search_monitor(self, device_id):
        pass

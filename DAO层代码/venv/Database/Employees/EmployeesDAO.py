from abc import ABC, abstractmethod


class EmployeesDAO(ABC):
    @abstractmethod
    def get_all_employees(self):
        pass

    @abstractmethod
    def create_employees(self, employee):
        pass

from abc import ABC, abstractmethod
from ctypes import Array


class Tire(ABC):
    def __init__(self, tire_wear_array: Array[int]):
        self.tire_wear_array=tire_wear_array
    @abstractmethod
    def need_service(self):
        pass
        
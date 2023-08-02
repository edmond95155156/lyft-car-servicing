"""from abc import ABC

from car import Car"""
from engine_interface import Engine

"""class CapuletEngine(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 30000"""

class CapuletEngine(Engine):
    def __init__(self, last_service_mileage:int,  current_mileage: int):
        self.last_service_mileage=last_service_mileage
        self.current_mileage=current_mileage
    
    def need_service(self):
        return self.current_mileage - self.last_service_mileage > 30000


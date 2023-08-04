from car import Car
from datetime import datetime
from  engine.capulet_engine import CapuletEngine
from  engine.sternman_engine import SternmanEngine
from  engine.willoughby_engine import WilloughbyEngine

from  battery.nubbin_battery import NubbinBattery
from  battery.spindler_battery import SpindlerBattery

class CarFactory:

    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        return Car(
            CapuletEngine(last_service_mileage, current_mileage),
            SpindlerBattery(last_service_date, current_date)
        )
    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int): 
        return Car(
            WilloughbyEngine(last_service_mileage, current_mileage), 
            SpindlerBattery(last_service_date, current_date)
        )
    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_on: bool): 
        return Car(
            SternmanEngine(warning_light_on), 
            SpindlerBattery(last_service_date, current_date)
        )
    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int): 
        return Car(
            WilloughbyEngine(last_service_mileage, current_mileage),
            NubbinBattery(last_service_date, current_date)
        )
    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        return Car(
            CapuletEngine(last_service_mileage, current_mileage),
            NubbinBattery(last_service_date, current_date)
        )





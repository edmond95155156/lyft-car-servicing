from engine.engine_interface import Engine
from battery.battery_interface import Battery
from serviceable import Serviceable
from tire.tire_interface import Tire
"""class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass"""


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tire: Tire):
        self.engine=engine
        self.battery=battery 
        self.tire=tire

    def needs_service(self):
        return self.engine.need_service() or self.battery.need_service() or self.tire.need_service()

    

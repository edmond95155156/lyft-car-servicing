from .tire_interface import Tire

class OctoprimeTire(Tire):
    def need_service(self):
        return sum(self.tire_wear_array) >=3
from .tire_interface import Tire

class CarriganTire(Tire):
    def need_service(self):
        return max(self.tire_wear_array)>=0.9
        

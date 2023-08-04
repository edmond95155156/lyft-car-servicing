from  .battery_interface import Battery
from datetime import datetime

class NubbinBattery(Battery):
    def __init__(self, last_service_date:datetime, current_date:datetime):
        self.last_service_date=last_service_date
        self.current_date=current_date

    def need_service(self):
        service_threshold_date=self.last_service_date.replace(year=self.last_service_date.year+4)
        return self.current_date > service_threshold_date

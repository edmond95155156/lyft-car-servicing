from battery_interface import Battery
from datetime import datetime

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date=last_service_date
        self.current_date=current_date

    def need_service(self, dateTime: datetime):
        service_threshold_date=dateTime.replace(year=dateTime.year+2)
        return datetime.today().date() > service_threshold_date

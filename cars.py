from car_factory import CarFactory
from serviceable import Serviceable

class Calliope(Serviceable):
    def needs_service(self):
        return CarFactory.create_calliope.needs_service()
class Glissade(Serviceable):
    def needs_service(self):
        return CarFactory.create_glissade.needs_service()
class Palindrome(Serviceable):
    def needs_service(self):
        return CarFactory.create_palindrome.needs_service()
class Rorschach(Serviceable):
    def needs_service(self):
        return CarFactory.create_rorschach.needs_service()
class Thovex(Serviceable):
    def needs_service(self):
        return CarFactory.create_thovex.needs_service()



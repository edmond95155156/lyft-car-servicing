import unittest

from app.engine.capulet_engine import CapuletEngine
from app.engine.sternman_engine import SternmanEngine
from app.engine.willoughby_engine import  WilloughbyEngine
from app.battery.spindler_battery import SpindlerBattery
from app.battery.nubbin_battery import NubbinBattery
from app.tire.carrigan_tire import CarriganTire
from app.tire.octoprime_tire import OctoprimeTire
from common_function import CommonFunction as CF

class CapuleEngineTest(unittest.TestCase):#30000 Miles
    def test_LessThan30000(self): 
        #self.assertTrue( False)  
        self.assertFalse( CapuletEngine(0,  29999).need_service())  
    def test_EqualTo30000(self): 
        self.assertFalse( CapuletEngine(0,  30000).need_service())  
    def test_LargerThan30000(self):
        self.assertTrue( CapuletEngine(0,  30001).need_service())  
class WilloughbyEngineTest(unittest.TestCase): #60000 Miles
    def test_LessThan60000(self): 
        self.assertFalse( WilloughbyEngine(0,  59999).need_service())  
    def test_EqualTo60000(self): 
        self.assertFalse( WilloughbyEngine(0,  60000).need_service())  
    def test_LargerThan60000(self):
        self.assertTrue( WilloughbyEngine(0,  60001).need_service())  
class SternmanEngineTest(unittest.TestCase): #Warning Indicator
    def test_WarningIndicatorOn(self):
        self.assertTrue( SternmanEngine(True).need_service())  
    def test_WarningIndicatorOff(self):
        self.assertFalse( SternmanEngine(False).need_service())  
class SpindlerBatteryTest(unittest.TestCase):
    def test_LessThan3Y(self):
        self.assertFalse(SpindlerBattery(CF.dateConvert("01-01-2020"),CF.dateConvert("31-12-2022")).need_service())
    def test_EqualTo3Y(self):
        self.assertFalse(SpindlerBattery(CF.dateConvert("01-01-2020"),CF.dateConvert("01-01-2023")).need_service())
    def test_LargerThan3Y(self):
        self.assertTrue(SpindlerBattery(CF.dateConvert("01-01-2020"),CF.dateConvert("02-01-2023")).need_service())
class NubbinBatteryTest(unittest.TestCase):
    def test_LessThan4Y(self):
        self.assertFalse(NubbinBattery(CF.dateConvert("01-01-2020"),CF.dateConvert("31-12-2023")).need_service())
    def test_EqualTo4Y(self):
        self.assertFalse(NubbinBattery(CF.dateConvert("01-01-2020"),CF.dateConvert("01-01-2024")).need_service())
    def test_LargerThan4Y(self):
        self.assertTrue(NubbinBattery(CF.dateConvert("01-01-2020"),CF.dateConvert("02-01-2024")).need_service())
class CarriganTireTest(unittest.TestCase):# one or more of the value at least 0.9.
    def test_0(self):
       self.assertFalse(CarriganTire([0.5,0.5,0.8,0.8]).need_service())
    def test_1(self):
        self.assertTrue(CarriganTire([0.5,0.5,0.9,0.9]).need_service())
    def test_2(self):
        self.assertTrue(CarriganTire([0.5,1,0.7,0.9]).need_service())
    def test_3(self):
        self.assertTrue(CarriganTire([0.5,1,0.7,1]).need_service())
class OctoprimeTireTest(unittest.TestCase): #sum at least 3
    def test_0(self):
        self.assertFalse(OctoprimeTire([0.7,0.8,0.9,0.5]).need_service())
    def test_1(self):
        self.assertTrue(OctoprimeTire([0.7,0.8,0.9,0.6]).need_service())
    def test_2(self):
        self.assertTrue(OctoprimeTire([0.7,0.8,0.9,0.7]).need_service())




if __name__ == '__main__':
    unittest.main()
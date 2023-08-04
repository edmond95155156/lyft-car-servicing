import unittest

from app.engine.capulet_engine import CapuletEngine
from app.engine.sternman_engine import SternmanEngine
from app.engine.willoughby_engine import  WilloughbyEngine
from app.battery.spindler_battery import SpindlerBattery
from app.battery.nubbin_battery import NubbinBattery
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
    def test_LessThan2Y(self):
        self.assertFalse(SpindlerBattery(CF.dateConvert("01-01-2020"),CF.dateConvert("31-12-2021")).need_service())
    def test_EqualTo2Y(self):
        self.assertFalse(SpindlerBattery(CF.dateConvert("01-01-2020"),CF.dateConvert("01-01-2022")).need_service())
    def test_LargerThan2Y(self):
        self.assertTrue(SpindlerBattery(CF.dateConvert("01-01-2020"),CF.dateConvert("02-01-2022")).need_service())
class NubbinBatteryTest(unittest.TestCase):
    def test_LessThan4Y(self):
        self.assertFalse(NubbinBattery(CF.dateConvert("01-01-2020"),CF.dateConvert("31-12-2023")).need_service())
    def test_EqualTo4Y(self):
        self.assertFalse(NubbinBattery(CF.dateConvert("01-01-2020"),CF.dateConvert("01-01-2024")).need_service())
    def test_LargerThan4Y(self):
        self.assertTrue(NubbinBattery(CF.dateConvert("01-01-2020"),CF.dateConvert("02-01-2024")).need_service())



if __name__ == '__main__':
    unittest.main()
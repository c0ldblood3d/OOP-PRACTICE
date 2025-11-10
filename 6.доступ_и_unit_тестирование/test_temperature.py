from categorize_temperature import categorize_temperature
import unittest

class TestCategorizeTemperature(unittest.TestCase):

    def test_freezing_temperatures(self):
        self.assertEqual(categorize_temperature(-10), "freezing")
        self.assertEqual(categorize_temperature(-5), "freezing")
        self.assertEqual(categorize_temperature(-1), "freezing")
        self.assertEqual(categorize_temperature(0), "freezing")
    
    def test_cold_temperatures(self):
        self.assertEqual(categorize_temperature(1), "cold")
        self.assertEqual(categorize_temperature(5), "cold")
        self.assertEqual(categorize_temperature(10), "cold")
    
    def test_cool_temperatures(self):
        self.assertEqual(categorize_temperature(11), "cool")
        self.assertEqual(categorize_temperature(15), "cool")
        self.assertEqual(categorize_temperature(20), "cool")
    
    def test_warm_temperatures(self):
        self.assertEqual(categorize_temperature(21), "warm")
        self.assertEqual(categorize_temperature(25), "warm")
        self.assertEqual(categorize_temperature(30), "warm")
    
    def test_hot_temperatures(self):
        self.assertEqual(categorize_temperature(31), "hot")
        self.assertEqual(categorize_temperature(35), "hot")
        self.assertEqual(categorize_temperature(40), "hot")
        self.assertEqual(categorize_temperature(100), "hot")
    
    def test_boundary_values(self):
        self.assertEqual(categorize_temperature(0), "freezing")
        self.assertEqual(categorize_temperature(1), "cold")
        
        self.assertEqual(categorize_temperature(10), "cold")
        self.assertEqual(categorize_temperature(11), "cool")
        
        self.assertEqual(categorize_temperature(20), "cool")
        self.assertEqual(categorize_temperature(21), "warm")
        
        self.assertEqual(categorize_temperature(30), "warm")
        self.assertEqual(categorize_temperature(31), "hot")
    
    def test_negative_extreme(self):
        self.assertEqual(categorize_temperature(-100), "freezing")
        self.assertEqual(categorize_temperature(-50), "freezing")
        self.assertEqual(categorize_temperature(-273), "freezing")  
    
    def test_positive_extreme(self):
        self.assertEqual(categorize_temperature(1000), "hot")
        self.assertEqual(categorize_temperature(500), "hot")
        self.assertEqual(categorize_temperature(100), "hot")

    def test_decimal_value(self):
        self.assertEqual(categorize_temperature(0.5), "cold")
        self.assertEqual(categorize_temperature(15.3333), "cool")
        self.assertEqual(categorize_temperature(31.9999999999), "hot")
        self.assertEqual(categorize_temperature(-15.32), "freezing")

if __name__ == '__main__':
    unittest.main(verbosity=2)
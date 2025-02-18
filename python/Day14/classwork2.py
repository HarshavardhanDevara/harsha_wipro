import unittest
 
import calculator
 
class TestCalculator(unittest.TestCase):
 
    def test_add(self):
 
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-1, -1), -2)
        self.assertEqual(calculator.add(0, 0), 0)
        
        
#python -m unittest test_calculator.py
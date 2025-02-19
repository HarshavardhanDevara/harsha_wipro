import unittest
 
import calculator
 
class TestCalculator(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 4)
        self.assertEqual(calculator.divide(9, 3), 3)
        self.assertEqual(calculator.divide(-6, 2), -3)
        self.assertEqual(calculator.divide(0, 1), 0)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(10, 0)
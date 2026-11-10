# https://github.com/hamiltona1-1/lab11-AH-JW
# Partner 1: Alexander Hamilton
# Partner 2: Jacob Wilson

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -5), -10)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(-2, -2), 0)

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(7, 0), 18)
        self.assertEqual(multiply(-7, 7), -49)
        self.assertEqual(multiply(-2, -1), 2)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(4, 2), 2.0)
        self.assertEqual(divide(10, 2), 0.2)
        self.assertEqual(divide(6, -18), -3.0)
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 8), 3.0)
        self.assertEqual(logarithm(10, 100), 2.0)
        self.assertEqual(logarithm(3, 9), 2.0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 5)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(6, -8), 10.0)
        self.assertEqual(hypotenuse(-5, -12), 13.0)
        self.assertEqual(hypotenuse(8, 15), 17.0)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-8)
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(100), 10)
        self.assertEqual(square_root(0), 0)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
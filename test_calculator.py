import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(7, 0), 18)
        self.assertEqual(multiply(-7, 7), -49)
        self.assertEqual(multiply(-2, -1), 2)
        # self.assertEqual(mul(7, 0), 18)
        # self.assertEqual(mul(-7, 7), -49)
        # self.assertEqual(mul(-2, -1), 2)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(4, 2), 2.0)
        self.assertEqual(divide(10, 2), 0.2)
        self.assertEqual(divide(6, -18), -3.0)
        # self.assertEqual(div(4, 2), 2.0)
        # self.assertEqual(div(10, 2), 0.2)
        # self.assertEqual(div(6, -18), -3.0)
    ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
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
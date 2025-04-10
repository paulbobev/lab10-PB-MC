#https://github.com/paulbobev/lab10-PB-MC.git
# Partner 1: Paul Bobev
# Partner 2: Mia Ciceri



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
        self.assertEqual(mul(2, 3), 6)          
        self.assertEqual(mul(-1, 5), -5)   
        self.assertEqual(mul(0, 100), 0)        

    def test_divide(self): # 3 assertions
        self.assertEqual(div(10, 2), 5)            
        self.assertAlmostEqual(div(7, 3), 2.3333, 4)  
        with self.assertRaises(ZeroDivisionError):      
            div(5, 0)

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
    
    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)  # Invalid base (0)



    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5.0)             # 3-4-5 triangle
        self.assertEqual(hypotenuse(5, 12), 13.0)           # 5-12-13 triangle
        self.assertAlmostEqual(hypotenuse(1.5, 2.5), math.sqrt(1.5**2 + 2.5**2), places=6)  # float input



    def test_sqrt(self): # 3 assertions
        if self < 0:
            raise ValueError("Cannot take square root of negative number.")
        return math.sqrt(self)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
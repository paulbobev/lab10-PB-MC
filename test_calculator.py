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
    def test_log_invalid_argument(a,b): # 1 assertion
        if a <= 0 or a == 1:
            raise ValueError("Base 'a' must be positive and not equal to 1.")
        if b <= 0:
            raise ValueError("Argument 'b' must be positive.")
        return math.log(b, a)


    def test_hypotenuse(a,b): # 3 assertions
        return math.sqrt(a ** 2 + b ** 2)


    def test_sqrt(x): # 3 assertions
        if self < 0:
            raise ValueError("Cannot take square root of negative number.")
        return math.sqrt(x)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
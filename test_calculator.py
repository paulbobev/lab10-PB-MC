#https://github.com/paulbobev/lab10-PB-MC.git
# Partner 1: Paul Bobev
# Partner 2: Mia Ciceri



import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(4, 1), 5)
        self.assertEqual(add(1, 3), 4)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(6, 3), 3)
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(9, 2), 7)
    ###########################

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
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(10, 100), 2.0)
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        self.assertAlmostEqual(logarithm(5, 25), 2.0)


    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 100)

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
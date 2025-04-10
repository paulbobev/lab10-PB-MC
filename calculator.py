"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def add(a, b): 
    return a + b
def subtract(a, b): 
    return a - b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):   # raise ZeroDivisionError if a == 0
    return b / a
def logarithm(a, b):     # use math library/raise ValueError
    return math.log(a,b)
def exponent(a, b): 
    return math.pow(a,b)
def square_root(a): 
    try:
        return math.sqrt(a) # raise ValueError if a < 0
    except:
        print("error")
try:
    def hypotenuse(a, b): 
        return math.hypot(a, b) # can have negative nums
except:
    print("No Negative Numbers")

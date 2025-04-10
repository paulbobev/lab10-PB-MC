"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math


# First example
def add(a, b): 
    return (a + b)

def subtract(a, b):
    return (a - b)

def mul(a, b):
    return (a * b)

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return (b / a)

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Values must be positive.")
    return math.log(a, b)

def exp(a, b):
    return (a ** b)
def hypotenuse(a, b): 
    if a < 0 or b < 0:
        raise ValueError("Values must be positive.")
    return math.hypot(a, b) # can have negative nums

def square_root(a):
    if a<0:
         raise ValueError("Values must be positive.")
    return math.sqrt(a)# raise ValueError if a < 0
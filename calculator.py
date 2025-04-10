#https://github.com/paulbobev/lab10-PB-MC.git
# Partner 1: Paul Bobev
# Partner 2: Mia Ciceri
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
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return (a / b)

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Base must be positive and not equal to 1.")
    if b <= 0:
        raise ValueError("Argument must be positive.")
    return math.log(b, a)

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
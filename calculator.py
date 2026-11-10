# https://github.com/hamiltona1-1/lab11-AH-JW
# Partner 1: Alexander Hamilton
# Partner 2: Jacob Wilson

import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    if (a <= 0) or (b <= 0) or (a == 1):
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a ** b
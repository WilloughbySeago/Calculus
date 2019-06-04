"""
This is a collection of functions related to differentiation
"""
from decimal import *

getcontext().rounding = ROUND_HALF_UP


def derivative(function, x, h=Decimal(0.0000000000010000000)):
    f_of_x = function(Decimal(x))
    f_of_x_plus_h = function(x + h)
    dy_dx = (f_of_x_plus_h - f_of_x) / h
    return round(dy_dx, 10)

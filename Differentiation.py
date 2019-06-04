"""
This is a collection of functions related to differentiation
"""
from decimal import *
from error import *

getcontext().rounding = ROUND_HALF_UP
getcontext().prec = 64


def derivative(function, x, h=Decimal(0.0000000000010000000)):
    """
    This function will approximate the derivative of a single variable function using:
    dy/dx = (f(x+h) - f(x))/h
    :param function: function (1 argument)
    :param x: int, float, Decimal
    :param h: int, float, Decimal
    :return: Decimal
    """
    if h == 0:
        error('h cannot be 0')
        raise DivisionByZero
    f_of_x = function(Decimal(x))
    f_of_x_plus_h = function(x + h)
    dy_dx = (f_of_x_plus_h - f_of_x) / h
    return round(dy_dx, 10)

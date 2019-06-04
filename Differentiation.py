"""
This is a collection of functions related to differentiation
"""
from decimal import *
from error import *
import math

getcontext().rounding = ROUND_HALF_UP
getcontext().prec = 64


def derivative1(function, x, h=Decimal(0.000000000000000100000000), decimal_places=10):
    """
    This function will approximate the derivative of a single variable function using:
    dy/dx = (f(x+h) - f(x))/h
    which is less accurate than the derivative2 method as this has first order errors
    :param function: function (1 argument)
    :param x: int, float, Decimal
    :param h: int, float, Decimal
    :param decimal_places: int
    :return: Decimal
    """
    if h == 0:
        error('h cannot be 0')
        raise DivisionByZero
    x = Decimal(x)
    h = Decimal(h)
    f_of_x = function(x)
    f_of_x_plus_h = function(x + h)
    dy_dx = (f_of_x_plus_h - f_of_x) / h
    return round(dy_dx, decimal_places)


def derivative2(function, x, h=Decimal(0.000000000000000100000000), decimal_places=10):
    """
    This function will approximate the derivative of a single variable function using:
    dy/dx = (f(x+h) - f(x-h))/(2h)
    which is more accurate than the derivative1 method as in this version all errors are second order
    :param function: function
    :param x: int, float, Decimal
    :param h: int, float, Decimal
    :param decimal_places: int
    :return: Decimal
    """
    if h == 0:
        error('h cannot be 0')
        raise DivisionByZero
    x = Decimal(x)
    h = Decimal(h)
    f_of_x_plus_h = function(x + h)
    f_of_x_minus_h = function(x - h)
    dy_dx = (f_of_x_plus_h - f_of_x_minus_h) / (2 * h)
    return round(dy_dx, decimal_places)


def newton_raphson(function, d_function, x_0, repeats, count=0):
    try:
        x_1 = Decimal(x_0) - Decimal(function(x_0)) / Decimal(d_function(x_0))
    except DivisionByZero:
        x_1 = Decimal(x_0) - Decimal(function(x_0)) / Decimal(0.0000000001)
    while count < repeats:
        count += 1
        return newton_raphson(function, d_function, x_1, repeats, count)
    return x_1

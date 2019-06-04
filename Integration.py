"""
This is a collection of integration related functions
"""
from decimal import *

getcontext().rounding = ROUND_HALF_UP
getcontext().prec = 64


def trapezium_rule(function, a, b, n):
    h = Decimal(b - a) / n
    y_values = []
    x = a
    for i in range(0, n):
        y = function(a + i * h)
        y_values.append(y)
    integral = y_values.pop(0) + y_values.pop(-1)
    integral += 2 * sum(y_values)
    integral *= Decimal(1 / 2)
    integral *= h
    return integral

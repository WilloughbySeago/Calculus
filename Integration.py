"""
This is a collection of integration related functions
"""
from decimal import *

getcontext().rounding = ROUND_HALF_UP
getcontext().prec = 64


def trapezium_rule(function, a, b, n):
    """
    This function applies the trapezium rule to a function

    ∫_a^b y dx = 1/2 * h[(y_0+y_n) + 2(Σ_(i=1)^(n-1) y_i)]
    h = (b - a) / n
    :param function: function
    :param a: int, float, Decimal
    :param b: int, float, Decimal
    :param n: int
    :return: Decimal
    """
    h = Decimal(b - a) / n
    y_values = []
    x = a
    for i in range(0, n):
        y = function(a + i * h)
        y_values.append(y)
    y_0, y_n = 0, 0
    try:
        y_0 = y_values.pop(0)
    except IndexError:
        pass
    try:
        y_n = y_values.pop(-1)
    except IndexError:
        pass
    integral = y_0 + y_n
    integral += 2 * sum(y_values)
    integral *= Decimal(1 / 2)
    integral *= h
    return integral

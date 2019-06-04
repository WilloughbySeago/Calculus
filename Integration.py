"""
This is a collection of integration related functions
"""
from decimal import *
from error import *

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
    if n == 0:
        error('n cannot be 0')
        raise DivisionByZero
    # If a > b then calculate -∫_b^a y dx
    invert = False
    if a > b:
        a, b = b, a
        invert = True
    h = Decimal(b - a) / n
    y_values = []
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
    if invert:
        return -integral
    else:
        return integral


def simpsons_rule(function, a, b, n):
    if n == 0:
        error('n cannot be 0')
        raise DivisionByZero
    invert = False
    if a > b:
        invert = True
        a, b = b, a
    h = Decimal(b - a) / n
    y_values = []
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
    odd_index, even_index = [], []
    for i in range(len(y_values)):
        if i % 2 + 1 == 1:  # since y_0 has been removed the firs item is y_1 is odd
            odd_index.append(y_values[i])
        else:
            even_index.append(y_values[i])
    integral = y_0 + y_n
    integral += 4 * sum(odd_index)
    integral += 2 * sum(even_index)
    integral *= Decimal(1 / 3)
    integral *= h
    if invert:
        return -integral
    else:
        return integral

#!/usr/bin/env python3
"""function that calculates a summation"""


def summation_i_squared(n):
    """function that returns the result of the summation"""
    if type(n) is not int or n < 1:
        return None
    return (n*(n + 1) * (2*n + 1))//6

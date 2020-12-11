#!/usr/bin/env python3
"""function that calculates a derivative"""


def poly_derivative(poly):
    """function that calculates the derivative of a polynomial"""
    if not poly or type(poly) is not list:
        return None

    anwser = []

    for order in range(1, len(poly)):
        anwser.append(order * poly[order])

    if not anwser:
        anwser.append(0)

    return anwser

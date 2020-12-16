#!/usr/bin/env python3
"""A function matrix_shape(matrix): that calculates the shape of a matrix"""


def matrix_shape(matrix):
    """Funtion shape"""
    shape = []
    if type(matrix) is list:
        shape.append(len(matrix))
        shape += matrix_shape(matrix[0])
    return shape

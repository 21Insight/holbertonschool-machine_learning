#!/usr/bin/env python3
import numpy as np
"""A function def matrix_shape(matrix): that calculates the shape of a matrix"""


def matrix_shape(matrix):
    """Funtion shape of numpy"""
    shape = list(np.shape(matrix))
    return shape

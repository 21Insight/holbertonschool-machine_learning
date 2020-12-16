#!/usr/bin/env python3
"""Adds two matrices element-wise"""


def get_length(rows):
    """Function used to calculate the length"""
    if rows and (type(rows) is list or type(rows) is tuple):
        return [len(rows), *get_length(rows[0])]
    return []



def matrix_shape(matrix):
    """Calculates the shape of a matrix"""
    return [*get_length(matrix)]


def add_matrices2D(mat1, mat2):
    """Adds two matrices 2D"""

    if matrix_shape(mat1) != matrix_shape(mat2):
        return None

    range_ax0 = range(len(mat1))
    range_ax1 = range(len(mat1[0]))

    return [[mat1[i][j] + mat2[i][j] for j in range_ax1] for i in range_ax0]

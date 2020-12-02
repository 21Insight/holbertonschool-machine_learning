#!/usr/bin/env python3
"""Returns the transpose of a 2D matrix"""


def matrix_transpose(matrix):
    """Calcuates the transpose of a matrix"""
    range_ax0 = range(len(matrix[0]))
    range_ax1 = range(len(matrix))

    return [[matrix[j][i] for j in range_ax1] for i in range_ax0]

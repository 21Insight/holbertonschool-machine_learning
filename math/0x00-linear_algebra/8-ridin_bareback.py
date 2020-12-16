#!/usr/bin/env python3
"""Performs matrix multiplication"""


def mat_mul(mat1, mat2):
    """Multiplicates two 2D matrices"""
    if len(mat1[0]) != len(mat2):
        return None

    range1 = range(len(mat1))
    range2 = range(len(mat2[0]))
    rax = range(len(mat1[0]))

    result = [[sum([mat1[i][k] * mat2[k][j] for k in rax])
               for j in range2] for i in range1]
    return result


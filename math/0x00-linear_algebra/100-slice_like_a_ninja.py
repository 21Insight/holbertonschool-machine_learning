#!/usr/bin/env python3
"""Slices a matrix along a specific axes"""


def np_slice(matrix, axes={}):
    """Slices a passed matrix with some specified axis"""
    hight_axis = max(axes, key=int) + 1
    slice_obj = tuple([slice(*axes.get(i) or (None,))
                       for i in range(hight_axis)])
    return matrix[slice_obj]


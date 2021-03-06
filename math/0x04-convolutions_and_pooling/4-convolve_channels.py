#!/usr/bin/env python3
"""Convolve channels"""
import numpy as np


def convolve_channels(images, kernel, padding='same', stride=(1, 1)):
    """Performs a convolution on images with channels"""
    m, h, w, c = images.shape
    kh, kw, c = kernel.shape
    sh, sw = stride

    if padding == 'valid':
        ph = 0
        pw = 0
    elif padding == 'same':
        ph = int((((h - 1) * sh + kh - h) / 2) + 1)
        pw = int((((w - 1) * sw + kw - w) / 2) + 1)
    else:
        ph, pw = padding

    oh = int(((h + 2 * ph - kh) / sh) + 1)
    ow = int(((w + 2 * pw - kw) / sw) + 1)

    input_pd = np.pad(
        images,
        ((0, 0), (ph, ph), (pw, pw), (0, 0)),
        'constant'
    )

    output = np.zeros((m, oh, ow))
    rng_im = np.arange(m)

    for i_oh in range(oh):
        for i_ow in range(ow):
            s_i_oh = i_oh * sh
            s_i_ow = i_ow * sw
            flt = input_pd[rng_im, s_i_oh:kh+s_i_oh, s_i_ow:kw+s_i_ow, :]
            output[rng_im, i_oh, i_ow] = np.sum(flt * kernel, axis=(1, 2, 3))
    return output

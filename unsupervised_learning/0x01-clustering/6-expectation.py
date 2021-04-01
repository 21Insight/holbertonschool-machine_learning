#!/usr/bin/env python3
"""
Calculates the expectation step in tne EM algorithm for a GMM
"""


import numpy as np
pdf = __import__('5-pdf').pdf


def expectation(X, pi, m, S):
    """
    Asign instances to clusters EM for GMM
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None
    if not isinstance(pi, np.ndarray) or len(pi.shape) != 1:
        return None, None
    if not isinstance(m, np.ndarray) or len(m.shape) != 2:
        return None, None
    if not isinstance(S, np.ndarray) or len(S.shape) != 3:
        return None, None
    if X.shape[1] != m.shape[1] != S.shape[1] != S.shape[2]:
        return None, None
    if pi.shape[0] != m.shape[0] != S.shappe[0]:
        return None, None

    n, d = X.shape
    k = pi.shape[0]
    if k > n:
        return None, None
    if k != m.shape[0] or k != S.shape[0]:
        return None, None
    if d != m.shape[1] or d != S.shape[1] or d != S.shape[2]:
        return None, None
    if not np.isclose([np.sum(pi)], [1])[0]:
        return None, None

    # create an array w/ kxn dimensionality
    g_arr = np.zeros((k, n))

    # probability for each datapoint to belong to
    # gaussian g
    for idx in range(k):

        # for each dataset, centroid means, cov matrix
        #  P contaiins all the pdf values
        P = pdf(X, m[idx], S[idx])

        # g_arr contains priors and pdf values
        g_arr[idx] = pi[idx] * P

    gSum = np.sum(g_arr, axis=0)
    g = g_arr / gSum

    # total log likelihood

    L = np.sum(np.log(gSum))

    return (g, L)

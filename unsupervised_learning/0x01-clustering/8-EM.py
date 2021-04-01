#!/usr/bin/env python3
""" clustering """

import numpy as np
initialize = __import__('4-initialize').initialize
expectation = __import__('6-expectation').expectation
maximization = __import__('7-maximization').maximization


def expectation_maximization(X, k, iterations=1000, tol=1e-5, verbose=False):
    """
    Performs the expectation maximization for a GMM
    """
    if type(X) is not np.ndarray or len(X.shape) != 2:
        return None, None, None, None, None
    if type(k) is not int or k <= 0:
        return None, None, None, None, None
    if type(iterations) is not int or iterations <= 0:
        return None, None, None, None, None
    if type(tol) is not float or tol < 0:
        return None, None, None, None, None
    if type(verbose) is not bool:
        return None, None, None, None, None

    i = 0
    l_prev = 0
    pi, mean, cov = initialize(X, k)
    g, log_like = expectation(X, pi, mean, cov)
    while i < iterations:
        if (np.abs(l_prev - log_like)) <= tol:
            break
        l_prev = log_like

        if verbose is True and (i % 10 == 0):
            rounded = log_like.round(5)
            print("Log Likelihood after {} iterations: {}".format(i, rounded))

        pi, mean, cov = maximization(X, g)
        g, log_like = expectation(X, pi, mean, cov)
        i += 1

    if verbose is True:
        rounded = log_like.round(5)
        print("Log Likelihood after {} iterations: {}".format(i, rounded))

    return pi, mean, cov, g, log_like

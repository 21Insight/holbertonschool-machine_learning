#!/usr/bin/env python3
""" clustering """
import sklearn.mixture


def gmm(X, k):
    """
    Calculates a GMM from a dataset
    """
    model = sklearn.mixture.GaussianMixture(n_components=k).fit(X)

    pi = model.weights_
    m = model.means_
    S = model.covariances_
    clss = model.predict(X)
    bic = model.bic(X)

    return pi, m, S, clss, bic

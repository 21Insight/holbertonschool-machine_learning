#!/usr/bin/env python3
""" clustering """
import sklearn.cluster


def kmeans(X, k):
    """
    Performs K-means on a dataset
    """
    k_means = sklearn.cluster.KMeans(n_clusters=k).fit(X)
    C = k_means.cluster_centers_
    clss = k_means.labels_
    return C, clss

'''
generate a sample dataset using Scikit-Learn's make_blobs function and compare the clustering labels generated by our cluster_data function with the true labels generated by make_blobs.
test three different clustering methods (kmeans, hierarchical, and dbscan) with different parameters to ensure that our clustering function is flexible and can handle different scenarios.
use assertEqual and assertLessEqual to check that the length of the clustering labels is equal to the length of the true labels and that the mean of the clustering labels is equal to the mean of the true labels.
'''

import unittest
import numpy as np
from sklearn.datasets import make_blobs
from clustering import cluster_data

class TestClustering(unittest.TestCase):

    def test_cluster_data(self):
        X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

        # test KMeans clustering
        kmeans_labels = cluster_data(X, method='kmeans', n_clusters=4)
        self.assertEqual(len(kmeans_labels), len(y_true))
        self.assertAlmostEqual(np.mean(kmeans_labels == y_true), 1.0, delta=0.05)

        # test hierarchical clustering
        hc_labels = cluster_data(X, method='hierarchical', n_clusters=4)
        self.assertEqual(len(hc_labels), len(y_true))
        self.assertAlmostEqual(np.mean(hc_labels == y_true), 1.0, delta=0.05)

        # test DBSCAN clustering
        dbscan_labels = cluster_data(X, method='dbscan', eps=0.5, min_samples=5)
        self.assertEqual(len(dbscan_labels), len(y_true))
        self.assertLessEqual(np.sum(dbscan_labels == -1), 10)
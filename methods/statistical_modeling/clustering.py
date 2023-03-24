'''
The load_data, scale_data, and perform_pca functions perform the data preprocessing steps.
The elbow_method function is used to determine the optimal number of clusters, and the kmeans_clustering function performs the actual clustering.
The plot_clusters function is used to visualize the resulting clusters.
Finally, the run_clustering_pipeline function runs the entire pipeline.
'''

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


def load_data(file_path):
    """Load data from file path"""
    return pd.read_csv(file_path)


def scale_data(data):
    """Scale the data using StandardScaler"""
    scaler = StandardScaler()
    return scaler.fit_transform(data)


def perform_pca(data, n_components):
    """Perform PCA on the data"""
    pca = PCA(n_components=n_components)
    return pca.fit_transform(data)


def elbow_method(data):
    """Use the elbow method to determine the optimal number of clusters"""
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
        kmeans.fit(data)
        wcss.append(kmeans.inertia_)
    plt.plot(range(1, 11), wcss)
    plt.title('Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()


def kmeans_clustering(data, n_clusters):
    """Perform k-means clustering on the data"""
    kmeans = KMeans(n_clusters=n_clusters, init='k-means++', max_iter=300, n_init=10, random_state=0)
    return kmeans.fit(data)


def plot_clusters(data, labels):
    """Plot the clusters"""
    plt.scatter(data[:, 0], data[:, 1], c=labels)
    plt.title('Clusters')
    plt.xlabel('PCA 1')
    plt.ylabel('PCA 2')
    plt.show()


def run_clustering_pipeline(file_path, n_components, n_clusters):
    """Run the full clustering pipeline"""
    data = load_data(file_path)
    scaled_data = scale_data(data)
    pca_data = perform_pca(scaled_data, n_components)
    elbow_method(pca_data)
    kmeans_model = kmeans_clustering(pca_data, n_clusters)
    plot_clusters(pca_data, kmeans_model.labels_)

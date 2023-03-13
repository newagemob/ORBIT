'''
PCA is a dimensionality reduction technique that is used to reduce the number of features in a dataset while retaining as much information as possible. It's a linear transformation that projects the data into a lower dimensional space. The new features are called principal components and are the directions of maximum variance in the data. The first principal component is the direction of maximum variance, the second principal component is the direction of maximum variance that is orthogonal to the first principal component, and so on.

This function takes in a pandas DataFrame and the desired number of components to keep after PCA, performs PCA on the features of the input DataFrame, and returns a transformed DataFrame with the specified number of components.

The function is modular and can be used with any DataFrame that has a 'target' column and any desired number of components. It uses the PCA class from scikit-learn to perform the dimensionality reduction.
'''

import pandas as pd
from sklearn.decomposition import PCA

def perform_pca(dataframe, n_components):
    """
    Perform Principal Component Analysis (PCA) on the given dataframe and
    return a transformed dataframe with n_components.

    Parameters:
    dataframe (pandas.DataFrame): Input dataframe.
    n_components (int): Number of components to keep after PCA.

    Returns:
    pandas.DataFrame: Transformed dataframe with n_components.
    """
    # Separate the features from the target variable
    features = dataframe.drop(columns=['target'])
    target = dataframe['target']

    # Create PCA object with the desired number of components
    pca = PCA(n_components=n_components)

    # Fit PCA on the features
    pca.fit(features)

    # Transform the features using the PCA object
    transformed = pca.transform(features)

    # Create a new dataframe with the transformed features and target variable
    cols = ['PC' + str(i+1) for i in range(n_components)]
    transformed_df = pd.DataFrame(transformed, columns=cols)
    transformed_df['target'] = target.values

    return transformed_df

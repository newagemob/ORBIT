'''
calculate_correlation function takes a DataFrame, and two feature names and calculates the Pearson correlation coefficient between those two features.
'''

import numpy as np

def calculate_correlation(df, feature1, feature2):
    """
    Calculate Pearson correlation coefficient between two features.

    Parameters:
    -----------
    df: pandas.DataFrame
        DataFrame containing the data to be used for the correlation analysis.
    feature1: str
        Name of the first feature to be used for the correlation analysis.
    feature2: str
        Name of the second feature to be used for the correlation analysis.

    Returns:
    --------
    corr_coef: float
        Pearson correlation coefficient between the two features.
    """

    # Calculate Pearson correlation coefficient between the two features
    corr_coef = np.corrcoef(df[feature1], df[feature2])[0, 1]

    return corr_coef

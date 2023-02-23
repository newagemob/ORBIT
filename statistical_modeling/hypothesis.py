'''
This script takes in a pandas DataFrame containing the data, the name of the feature to be used for grouping, and the labels for the two groups to be compared. It then conducts a two-sample t-test on the data and returns the t-statistic and p-value of the test.
'''

import pandas as pd
from scipy.stats import ttest_ind

def hypothesis_testing(data, feature, group1_label, group2_label):
    """
    Conducts two-sample t-test to determine if there is a significant difference in means
    between two groups based on a specific feature
    
    Parameters:
        - data: a pandas DataFrame containing the data
        - feature: a string representing the feature to be used for grouping
        - group1_label: a string representing the label for group 1
        - group2_label: a string representing the label for group 2
        
    Returns:
        - t_stat: the t-statistic of the test
        - p_val: the p-value of the test
    """
    # Separate data into two groups based on a certain feature
    group1 = data[data[feature] == group1_label]['price']
    group2 = data[data[feature] == group2_label]['price']

    # Conduct two-sample t-test to determine if there is a significant difference in means between the two groups
    t_stat, p_val = ttest_ind(group1, group2)

    # Print results
    print('t-statistic:', t_stat)
    print('p-value:', p_val)
    
    return t_stat, p_val


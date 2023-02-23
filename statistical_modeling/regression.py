'''
This script includes a class RegressionAnalysis that takes in the data file, target column, and feature columns as inputs. It has methods to add a constant term for intercept, fit a linear regression model, and return the summary statistics of the model.
'''

import pandas as pd
import statsmodels.api as sm
import unittest

class RegressionAnalysis:

    def __init__(self, data_file, target_col, feature_cols):
        self.df = pd.read_csv(data_file)
        self.X = self.df[feature_cols]
        self.y = self.df[target_col]

    def add_constant_term(self):
        self.X = sm.add_constant(self.X)

    def fit_linear_regression(self):
        self.model = sm.OLS(self.y, self.X).fit()

    def get_model_summary(self):
        return self.model.summary()

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import datetime as dt
from methods.data_analysis.data_visualization.machine_readable import MachineLearningData


class DecisionTree:
    '''
    This class builds a decision tree model using the data from the MachineLearningData class.

    The prediction model is built using the following features:
    - Annual Trend
    - Annual Spread
    - Annual Liquidity
    - Annual Volatility
    - Annual Momentum

    The target vector is the Annual Return.

    Prediction output is a classification of the Annual Return into three categories:
    - Low
    - Medium
    - High
    Represented by the numbers 0, 1, and 2 respectively. This prediction will be used to influence the portfolio allocation.
    '''

    def __init__(self, csv_file):
        self.visualizer = MachineLearningData(csv_file)

    def build_model(self):
        annual_trend = self.visualizer.determine_annual_trend()
        annual_spread = self.visualizer.determine_annual_spread()
        annual_liquidity = self.visualizer.determine_annual_liquidity()
        annual_volatility = self.visualizer.determine_annual_volatility()
        annual_momentum = self.visualizer.determine_annual_momentum()
        # Each of the above functions returns a pandas dataframe with two columns (Symbol, Annual ___)

        # create feature matrix -- this is the data used to predict the target vector
        X = pd.concat([annual_trend, annual_spread, annual_liquidity,
                      annual_volatility, annual_momentum], axis=1)

        # create target vector
        # extract only "Annual Return" column
        y = self.visualizer.determine_annual_return()["Annual Return"]
        y_classes = pd.cut(y, bins=3, labels=[0, 1, 2])

        # build decision tree model
        model = DecisionTreeClassifier()
        model.fit(X, y_classes)

        # make predictions
        y_pred = model.predict(X)
        print("Accuracy:", metrics.accuracy_score(y_classes, y_pred))
        print("Precision:", metrics.precision_score(
            y_classes, y_pred, average='weighted'))
        print("Preditction:", y_pred)
        return model

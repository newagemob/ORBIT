'''
Decision Tree Classifier

Receive input from HumanVisualization functions and output a decision tree classifier
'''

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import datetime as dt
from methods.data_analysis.data_visualization.human_readable import HumanVisualization

class DecisionTree:
    def __init__(self, csv_file):
        self.visualizer = HumanVisualization(csv_file)
        
    def build_model(self):
        annual_trend = self.visualizer.determine_annual_trend()
        annual_spread = self.visualizer.determine_annual_spread()
        annual_liquidity = self.visualizer.determine_annual_liquidity()
        annual_volatility = self.visualizer.determine_annual_volatility()
        annual_momentum = self.visualizer.determine_annual_momentum()

        # create feature matrix
        X = [[annual_trend[i], annual_spread[i], annual_liquidity[i], annual_volatility[i], annual_momentum[i]] for i in range(len(self.visualizer.data))]

        # create label vector
        y = [1 if self.visualizer.data['Change %'][i] > 0 else 0 for i in range(len(self.visualizer.data))]

        # build decision tree model
        model = DecisionTreeClassifier()
        model.fit(X, y)

        return model


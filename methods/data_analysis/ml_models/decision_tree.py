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
from methods.data_analysis.data_visualization.machine_readable import MachineLearningData

class DecisionTree:
    def __init__(self, csv_file):
        self.visualizer = MachineLearningData(csv_file)
        
    def build_model(self):
        annual_trend = self.visualizer.determine_annual_trend()
        annual_spread = self.visualizer.determine_annual_spread()
        annual_liquidity = self.visualizer.determine_annual_liquidity()
        annual_volatility = self.visualizer.determine_annual_volatility()
        annual_momentum = self.visualizer.determine_annual_momentum()
        # Each of the above functions returns a pandas dataframe with two columns (Symbol, Annual ___)

        # create feature matrix
        X = pd.concat([annual_trend, annual_spread, annual_liquidity, annual_volatility, annual_momentum], axis=1)

        # create target vector
        y = self.visualizer.determine_annual_return()
        

    
        # build decision tree model
        model = DecisionTreeClassifier()
        model.fit(X, y)

        return model
    
    def predict(self, model):
        


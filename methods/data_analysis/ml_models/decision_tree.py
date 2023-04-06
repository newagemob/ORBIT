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
        annual_volatility = self.visualizer.    determine_annual_volatility()
        annual_momentum = self.visualizer.determine_annual_momentum()
        # Each of the above functions returns a pandas dataframe with two columns (Symbol, Annual ___)

        # create feature matrix
        X = pd.concat([annual_trend, annual_spread, annual_liquidity, annual_volatility, annual_momentum], axis=1)

        # create target vector
        y = self.visualizer.determine_annual_return()["Annual Return"]  # extract only "Annual Return" column
        y_classes = pd.cut(y, bins=3, labels=[0, 1, 2])

        # build decision tree model
        model = DecisionTreeClassifier()
        model.fit(X, y_classes)

        # make predictions
        y_pred = model.predict(X)
        print("Accuracy:", metrics.accuracy_score(y_classes, y_pred))
        print("Precision:", metrics.precision_score(y_classes, y_pred, average='weighted'))
        print("Preditction:", y_pred)
        return model

    
if __name__ == '__main__':
    project_dir = Path(__file__).resolve().parents[3]
    csv_file = f"{project_dir}/methods/data_collection/output/SP500/yahoo_sp500_stocks_{dt.date.today()}.csv"
    decision_tree = DecisionTree(csv_file)
    model = decision_tree.build_model()

'''
This script defines a plot_line_chart function that takes in data and several optional parameters to customize the chart. The main function loads the data, prepares it, and calls the plot_line_chart function with the appropriate arguments.
'''

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

project_dir = Path(__file__).resolve().parents[3]

class LineChart:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)

    def plot_to
        """
        Plot a line chart using Matplotlib.

        Args:

        Returns:
        - Outputs a line chart
        """
        plt.title('Stock Line Chart')

        df = pd.read_csv(csv_file)
        for symbol in df['Symbol'].unique():
            symbol_df = df[df['Symbol'] == symbol]
            plt.plot(symbol_df['date'], symbol_df['Price'], label=symbol)
            
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

if __name__ == '__main__':
    csv_file = f'{project_dir}/methods/data_collection/output/SP500/sp500_stocks_2023-03-24.csv'
    LineChart.plot_line_chart(csv_file)

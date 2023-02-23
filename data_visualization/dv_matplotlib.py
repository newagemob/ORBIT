'''
This script defines a plot_line_chart function that takes in data and several optional parameters to customize the chart. The main function loads the data, prepares it, and calls the plot_line_chart function with the appropriate arguments.
'''

import pandas as pd
import matplotlib.pyplot as plt

def plot_line_chart(x, y, title='', xlabel='', ylabel='', figsize=(8, 6), savefig_path=None):
    """
    Plot a line chart using Matplotlib.

    Args:
    - x (array-like): x-axis data.
    - y (array-like): y-axis data.
    - title (str): chart title (default '').
    - xlabel (str): label for x-axis (default '').
    - ylabel (str): label for y-axis (default '').
    - figsize (tuple): size of the figure in inches (default (8, 6)).
    - savefig_path (str): path to save the figure (default None).

    Returns:
    - None
    """
    plt.figure(figsize=figsize)
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if savefig_path:
        plt.savefig(savefig_path)
    plt.show()

def main():
    # Load data
    df = pd.read_csv('data.csv')

    # Prepare data
    x = df['date']
    y = df['price']

    # Plot line chart
    plot_line_chart(x, y, title='Stock Price over Time', xlabel='Date', ylabel='Price', savefig_path='stock_price.png')

if __name__ == '__main__':
    main()

'''
Each of these functions is designed to be modular and can be used individually or combined to create custom data visualizations.

# Example usage
plot_scatter_chart('date', 'close', 'Stock Prices Over Time')
plot_histogram('close', 'Distribution of Closing Prices')
plot_line_chart('date', 'close', 'Stock Prices Over Time')
plot_bar_chart('date', 'volume', 'Daily Trading Volume')
plot_heatmap('day_of_week', 'hour_of_day', 'volume', 'Trading Volume by Day and Hour')

plot_scatter_chart: This function plots a scatter chart using Plotly, which is a type of chart that displays data points on a two-dimensional plane. This function takes in a Pandas DataFrame and x and y column names to plot.

plot_histogram: This function plots a histogram using Plotly, which is a type of chart that shows the distribution of a numerical variable. This function takes in a Pandas DataFrame and the column name to plot.

plot_line_chart: This function plots a line chart using Plotly, which is a type of chart that shows the trend of a variable over time or another continuous variable. This function takes in a Pandas DataFrame and x and y column names to plot.

plot_bar_chart: This function plots a bar chart using Plotly, which is a type of chart that displays categorical data with rectangular bars. This function takes in a Pandas DataFrame and x and y column names to plot.

plot_heatmap: This function plots a heatmap using Plotly, which is a type of chart that displays the magnitude of a numerical variable as colors on a grid. This function takes in a Pandas DataFrame and the column names for the x-axis, y-axis, and z-axis.
'''

import pandas as pd
import plotly.graph_objs as go
from pathlib import Path

project_dir = Path(__file__).resolve().parents[3]

# csv file will be fed into the class
class PlotlyVisualization:
    def __init__(self, data_collection_csv_file):
        self.df = pd.read_csv(data_collection_csv_file, parse_dates=['date'], index_col='date')

        df = pd.read_csv(f'{project_dir}/methods/data_collection/output/SP500/sp500_stocks_2023-03-24.csv')
        fig = go.Figure(data=[go.Candlestick(x=df['date'],
                        open=df['Price'],
                        high=df['Price'],
                        low=df['Price'],
                        close=df['Price'])])
        fig.show()


    def plot_scatter_chart(self, x_col, y_col, title):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=self.df[x_col], y=self.df[y_col],
                        mode='markers', name=y_col))
        fig.update_layout(title=title, xaxis_title=x_col, yaxis_title=y_col)
        fig.show()

    def plot_histogram(self, col, title):
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=self.df[col]))
        fig.update_layout(title=title, xaxis_title=col, yaxis_title='Frequency')
        fig.show()

    def plot_line_chart(self, x_col, y_col, title):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=self.df[x_col], y=self.df[y_col],
                        mode='lines', name=y_col))
        fig.update_layout(title=title, xaxis_title=x_col, yaxis_title=y_col)
        fig.show()

    def plot_bar_chart(self, x_col, y_col, title):
        fig = go.Figure()
        fig.add_trace(go.Bar(x=self.df[x_col], y=self.df[y_col]))
        fig.update_layout(title=title, xaxis_title=x_col, yaxis_title=y_col)
        fig.show()

    def plot_heatmap(self, x_col, y_col, z_col, title):
        fig = go.Figure(data=go.Heatmap(
            x=self.df[x_col],
            y=self.df[y_col],
            z=self.df[z_col],
            colorscale='Viridis'))
        fig.update_layout(title=title, xaxis_title=x_col, yaxis_title=y_col)
        fig.show()
        
        
if __name__ == '__main__':
    csv_file = f'{project_dir}/methods/data_collection/output/SP500/sp500_stocks_2023-03-24.csv'
    PlotlyVisualization(csv_file).plot_scatter_chart('date', 'Price', 'Stock Prices Over Time')
    PlotlyVisualization(csv_file).plot_histogram('Price', 'Distribution of Closing Prices')
    PlotlyVisualization(csv_file).plot_line_chart('date', 'Price', 'Stock Prices Over Time')
    PlotlyVisualization(csv_file).plot_bar_chart('date', 'Volume', 'Daily Trading Volume')
    PlotlyVisualization(csv_file).plot_heatmap('day_of_week', 'hour_of_day', 'Volume', 'Trading Volume by Day and Hour')

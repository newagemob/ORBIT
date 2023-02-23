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

# Read in cleaned data
df = pd.read_csv('cleaned_stock_data.csv')

def plot_scatter_chart(x_col, y_col, title):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df[x_col], y=df[y_col],
                    mode='markers', name=y_col))
    fig.update_layout(title=title, xaxis_title=x_col, yaxis_title=y_col)
    fig.show()

def plot_histogram(col, title):
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df[col]))
    fig.update_layout(title=title, xaxis_title=col, yaxis_title='Frequency')
    fig.show()

def plot_line_chart(x_col, y_col, title):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df[x_col], y=df[y_col],
                    mode='lines', name=y_col))
    fig.update_layout(title=title, xaxis_title=x_col, yaxis_title=y_col)
    fig.show()

def plot_bar_chart(x_col, y_col, title):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df[x_col], y=df[y_col]))
    fig.update_layout(title=title, xaxis_title=x_col, yaxis_title=y_col)
    fig.show()

def plot_heatmap(x_col, y_col, z_col, title):
    fig = go.Figure(data=go.Heatmap(
        x=df[x_col],
        y=df[y_col],
        z=df[z_col],
        colorscale='Viridis'))
    fig.update_layout(title=title, xaxis_title=x_col, yaxis_title=y_col)
    fig.show()

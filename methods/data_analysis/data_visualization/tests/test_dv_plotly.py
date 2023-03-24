import unittest
import pandas as pd
from methods.data_analysis.data_visualization.dv_plotly import PlotlyVisualization
from pathlib import Path

project_dir = Path(__file__).resolve().parents[3]

class TestPlotlyVisualization(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.test_file = f"{project_dir}/data_collection/output/SP500/sp500_stocks_2023-03-23.csv"
        cls.df = pd.read_csv(cls.test_file)
        cls.plotly = PlotlyVisualization(cls.test_file)

    def test_plot_scatter_chart(self):
        self.plotly.plot_scatter_chart('date', 'close', 'Stock Prices Over Time')
        # add assertions here if necessary

    def test_plot_histogram(self):
        self.plotly.plot_histogram('close', 'Distribution of Closing Prices')
        # add assertions here if necessary

    def test_plot_line_chart(self):
        self.plotly.plot_line_chart('date', 'close', 'Stock Prices Over Time')
        # add assertions here if necessary

    def test_plot_bar_chart(self):
        self.plotly.plot_bar_chart('date', 'volume', 'Daily Trading Volume')
        # add assertions here if necessary

    def test_plot_heatmap(self):
        self.plotly.plot_heatmap('day_of_week', 'hour_of_day', 'volume', 'Trading Volume by Day and Hour')
        # add assertions here if necessary

if __name__ == '__main__':
    unittest.main()

'''
Current Funds / Stocks: S&P 500

This is the second step in the ORBIT pipeline. This script visualizes the data for both human-readable and machine-readable purposes.
'''

from pathlib import Path
import datetime as dt
from methods.data_analysis.data_visualization.human_readable import HumanVisualization

methods_dir = Path(__file__).resolve().parents[2]

data_analysis = HumanVisualization(
    f'{methods_dir}/data_collection/output/SP500/yahoo_sp500_stocks_{dt.date.today()}.csv')

data_analysis.determine_annual_trend()
data_analysis.determine_annual_momentum()
data_analysis.determine_annual_spread()
data_analysis.determine_annual_volatility()
data_analysis.determine_annual_liquidity()

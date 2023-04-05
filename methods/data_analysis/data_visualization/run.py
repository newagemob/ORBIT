'''
Current Funds / Stocks: S&P 500

This is the second step in the ORBIT pipeline. This script visualizes the data for both human-readable and machine-readable purposes.
'''

import pandas as pd
from pathlib import Path
import datetime as dt
from methods.data_analysis.data_visualization.human_readable import HumanVisualization
from methods.data_analysis.data_visualization.machine_readable import MachineLearningData

methods_dir = Path(__file__).resolve().parents[2]

print(methods_dir)


def run_human_readable() -> None:
    data_analysis = HumanVisualization(
        f'{methods_dir}/data_collection/output/SP500/yahoo_sp500_stocks_{dt.date.today()}.csv')

    data_analysis.determine_annual_trend()
    data_analysis.determine_annual_spread()
    data_analysis.determine_annual_liquidity()
    data_analysis.determine_annual_volatility()
    data_analysis.determine_annual_momentum()

    # Look through the csv files output by each function and determine the top 10 annual companies for each category
    def top_10_annual_companies() -> None:
        """
        Looks through the csv files output by each function and determines the top 10 annual companies for each category.
        """
        # Create a dictionary of the csv files output by each function
        csv_files = {
            'trend': f'{methods_dir}/data_analysis/data_visualization/output/SP500/human_readable/annual_trend_{dt.date.today()}.csv',
            'momentum': f'{methods_dir}/data_analysis/data_visualization/output/SP500/human_readable/annual_momentum_{dt.date.today()}.csv',
            'spread': f'{methods_dir}/data_analysis/data_visualization/output/SP500/human_readable/annual_spread_{dt.date.today()}.csv',
            'volatility': f'{methods_dir}/data_analysis/data_visualization/output/SP500/human_readable/annual_volatility_{dt.date.today()}.csv',
            'liquidity': f'{methods_dir}/data_analysis/data_visualization/output/SP500/human_readable/annual_liquidity_{dt.date.today()}.csv'
        }
        # Create a dictionary of the top 10 annual companies for each category
        top_10_annual_companies = {
            'trend': [],
            'momentum': [],
            'spread': [],
            'volatility': [],
            'liquidity': []
        }
        # For each csv file in the dictionary, determine the top 10 annual companies for each category
        for symbol, csv_file in csv_files.items():
            # Read the csv file into a DataFrame
            df = pd.read_csv(csv_file)
            # For each column in the DataFrame, determine the top 10 annual companies for each category
            for column in df.columns:
                # Sort the DataFrame by the column
                df_sorted = df.sort_values(by=column, ascending=False)
                # Get the top 10 annual companies for each category
                top_10 = df_sorted.head(10)
                # Append the top 10 annual companies for each category to the dictionary
                top_10_annual_companies[symbol].append(top_10)

        # Create a DataFrame from the dictionary
        df_top_10_annual_companies = pd.DataFrame(top_10_annual_companies)
        # Write the DataFrame to a csv file
        df_top_10_annual_companies.to_csv(
            f'{methods_dir}/data_analysis/data_visualization/output/SP500/human_readable/top_10_annual_companies_{dt.date.today()}.csv', index=False)

    top_10_annual_companies()


def run_machine_readable() -> None:
    data_analysis = MachineLearningData(
        f'{methods_dir}/data_collection/output/SP500/yahoo_sp500_stocks_{dt.date.today()}.csv')

    data_analysis.determine_annual_trend()
    data_analysis.determine_annual_spread()
    data_analysis.determine_annual_liquidity()
    data_analysis.determine_annual_volatility()
    data_analysis.determine_annual_momentum()
    

run_human_readable()
run_machine_readable()

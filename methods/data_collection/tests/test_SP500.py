import unittest
from unittest.mock import patch
import pandas as pd
from io import StringIO
import os
from data_collection.SP500 import get_sp100

class TestSP500(unittest.TestCase):
    # use get_sp100 to get the top 100 stocks from the S&P 500 and save them to a CSV file
    def test_get_sp100(self):
        # Define input and output file paths
        input_file = './output/SP500.csv'
        output_file = './output/cleaned_SP500.csv'

        # Define start and end dates for time period to filter data
        start_date = pd.to_datetime('2022-01-01')
        end_date = pd.to_datetime('2022-12-31')

        # Clean and preprocess data
        df = get_sp100(input_file, output_file, start_date, end_date)

        # Check that the output file was created
        with open(output_file, 'r') as f:
            lines = f.readlines()
            self.assertGreater(len(lines), 0)

        # Check that the date range of the cleaned data is correct
        self.assertEqual(df['Date'].min(), start_date)
        self.assertEqual(df['Date'].max(), end_date)

        # Check that there are no missing values in the cleaned data
        self.assertEqual(df.isnull().sum().sum(), 0)

        # Check that the output file has the correct columns
        expected_columns = ['Date', 'Price']
        output_df = pd.read_csv(output_file)
        self.assertListEqual(list(output_df.columns), expected_columns)
        
if __name__ == "__main__":
    unittest.main()
    # get_sp100("data_collection/SP500.csv", 100, "1y")

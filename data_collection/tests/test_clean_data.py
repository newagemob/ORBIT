import pandas as pd
import unittest
from datetime import datetime

from data_collection.clean_data import clean_and_preprocess_data


class TestDataCleaning(unittest.TestCase):
    
    def test_clean_and_preprocess_data(self):
        
        # Define input and output file paths
        input_file = 'test_data.csv'
        output_file = 'test_output.csv'
        
        # Define start and end dates for time period to filter data
        start_date = pd.to_datetime('2022-01-01')
        end_date = pd.to_datetime('2022-12-31')
        
        # Create test data
        test_data = {'date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
                     'price': [100, 110, 90, 120, 115],
                     'column1': ['a', 'b', 'c', 'd', 'e'],
                     'column2': ['x', 'y', 'z', 'w', 'v']}
        df = pd.DataFrame(test_data)
        
        # Save test data to a csv file
        df.to_csv(input_file, index=False)
        
        # Call clean_and_preprocess_data function to clean test data
        result_df = clean_and_preprocess_data(input_file, output_file, start_date, end_date)
        
        # Check that the output file was created
        try:
            with open(output_file) as f:
                pass
        except FileNotFoundError:
            self.fail("Output file was not created.")
        
        # Check that the output file contains the expected data
        expected_data = {'Date': [pd.to_datetime('2022-01-02'), pd.to_datetime('2022-01-04'), pd.to_datetime('2022-01-05')],
                         'Price': [115, 120, 115]}
        expected_df = pd.DataFrame(expected_data)
        expected_df = expected_df.astype(result_df.dtypes)
        pd.testing.assert_frame_equal(result_df, expected_df)
        
        # Remove test files
        import os
        os.remove(input_file)
        os.remove(output_file)
        

if __name__ == '__main__':
    unittest.main()

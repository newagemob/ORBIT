import unittest
import pandas as pd
from out_of_sample import out_of_sample_test

class TestOutOfSample(unittest.TestCase):
    
    def test_out_of_sample(self):
        # Generate sample data
        data = pd.DataFrame({
            'date': pd.date_range(start='2022-01-01', end='2022-06-30'),
            'price': [100, 101, 105, 102, 99, 97, 103, 105, 110, 108, 111, 109, 107, 105, 103, 105, 108, 110, 112, 109, 106, 103, 100, 97, 95, 98, 100]
        })
        
        # Run out-of-sample test
        result = out_of_sample_test(data, 10, 5)
        
        # Assert that result is a pandas dataframe
        self.assertIsInstance(result, pd.DataFrame)
        
        # Assert that result has the correct number of rows
        self.assertEqual(len(result), 6)
        
        # Assert that result contains the expected columns
        expected_cols = ['date', 'predicted_return', 'actual_return', 'prediction_correct']
        self.assertListEqual(list(result.columns), expected_cols)
        
        # Assert that prediction_correct column has only True or False values
        self.assertTrue(result['prediction_correct'].isin([True, False]).all())

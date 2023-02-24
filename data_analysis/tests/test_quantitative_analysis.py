'''
This unit test checks if:

the function returns a dataframe with 3 rows for the tickers provided,
each ticker is included in the 'Ticker' column of the dataframe,
the R-Squared, ADF Statistic, and ADF p-value columns contain valid values (i.e., R-Squared >= 0, |ADF Statistic| >= 0, and ADF p-value <= 1).
'''

import unittest
from quant_analysis import quantitative_analysis as qa

class TestQuantitativeAnalysis(unittest.TestCase):
    
    def test_perform_quantitative_analysis_batch(self):
        tickers = ['AAPL', 'MSFT', 'GOOGL']
        results = qa.perform_quantitative_analysis_batch(tickers)
        self.assertEqual(len(results), 3)
        self.assertIn('AAPL', results['Ticker'].tolist())
        self.assertIn('MSFT', results['Ticker'].tolist())
        self.assertIn('GOOGL', results['Ticker'].tolist())
        self.assertTrue(all(results['R-Squared'] >= 0))
        self.assertTrue(all(abs(results['ADF Statistic']) >= 0))
        self.assertTrue(all(results['ADF p-value'] <= 1))

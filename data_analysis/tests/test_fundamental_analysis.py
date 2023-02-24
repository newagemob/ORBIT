

import unittest
from unittest.mock import patch
import pandas as pd
from fund_analysis import fundamental_analysis as fa

class TestFundamentalAnalysis(unittest.TestCase):

    @patch('yfinance.Ticker')
    def test_analyze_fundamentals(self, mock_ticker):
        # Define mock data for the ticker object
        mock_ticker.return_value.financials.loc.__getitem__.side_effect = [['Total Revenue', 'Gross Profit', 'Operating Income']]
        mock_ticker.return_value.balance_sheet.loc.__getitem__.side_effect = [['Total Assets', 'Total Liabilities', 'Total Stockholder Equity']]
        mock_ticker.return_value.cashflow.loc.__getitem__.side_effect = [['Total Cash From Operating Activities', 'Total Cashflows From Investing Activities', 'Total Cashflows From Financing Activities']]
        mock_ticker.return_value.history.return_value = pd.DataFrame({
            'Close': [100, 120, 110],
            'Earnings/Share': [10, 12, 11],
            'Book Value': [50, 60, 70],
            'Revenue/Share': [5, 6, 7]
        })

        # Call the function with a mock ticker symbol
        report = fa.analyze_fundamentals('AAPL')

        # Define expected output
        expected_report = {
            'ticker': 'AAPL',
            'income_statement': {'Total Revenue': {0: 5, 1: 6, 2: 7},
                                 'Gross Profit': {0: None, 1: None, 2: None},
                                 'Operating Income': {0: None, 1: None, 2: None}},
            'balance_sheet': {'Total Assets': {0: None, 1: None, 2: None},
                              'Total Liabilities': {0: None, 1: None, 2: None},
                              'Total Stockholder Equity': {0: None, 1: None, 2: None}},
            'cash_flow': {'Total Cash From Operating Activities': {0: None, 1: None, 2: None},
                           'Total Cashflows From Investing Activities': {0: None, 1: None, 2: None},
                           'Total Cashflows From Financing Activities': {0: None, 1: None, 2: None}},
            'financial_ratios': {'P/E Ratio': 10.0, 'P/B Ratio': 2.0, 'P/S Ratio': 20.0}
        }

        # Assert the output matches the expected output
        self.assertEqual(report, expected_report)

'''
In this unit test, we create a sample time series in the setUp method. We then define three test methods: test_arima, test_seasonal_arima, and test_forecast, each testing a different aspect of the TimeSeriesAnalyzer class.

test_arima method tests that the fit_arima method returns an instance of the ARIMA class when called with a (1,1,1) order.
test_seasonal_arima method tests that the fit_seasonal_arima method returns an instance of the ARIMA class when called with (1,1,1)x(1,1,1,12) orders.
test_forecast method tests that the forecast method returns a pandas series of length 10 when called with an ARIMA model with (1,1,1) order.
'''

import unittest
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from time_series_analysis import TimeSeriesAnalyzer


class TimeSeriesAnalyzerTest(unittest.TestCase):

    def setUp(self):
        # Create a sample time series for testing
        self.ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))

    def test_arima(self):
        # Test ARIMA model with (1,1,1) order
        analyzer = TimeSeriesAnalyzer(self.ts)
        model = analyzer.fit_arima(order=(1, 1, 1))
        self.assertIsInstance(model, ARIMA)

    def test_seasonal_arima(self):
        # Test seasonal ARIMA model with (1,1,1)x(1,1,1,12) orders
        analyzer = TimeSeriesAnalyzer(self.ts)
        model = analyzer.fit_seasonal_arima(order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
        self.assertIsInstance(model, ARIMA)

    def test_forecast(self):
        # Test forecasting with ARIMA model with (1,1,1) order
        analyzer = TimeSeriesAnalyzer(self.ts)
        model = analyzer.fit_arima(order=(1, 1, 1))
        forecast = analyzer.forecast(model, steps=10)
        self.assertIsInstance(forecast, pd.Series)
        self.assertEqual(len(forecast), 10)


if __name__ == '__main__':
    unittest.main()

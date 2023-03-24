'''
we have defined several functions for loading time series data, performing seasonal decomposition, running the Augmented Dickey-Fuller test, and fitting an ARMA model.
ADF (Augmented Dickey-Fuller) test is a statistical test that can be used to determine if a time series is stationary or not. A stationary time series is one whose statistical properties such as mean, variance, autocorrelation, etc. are all constant over time. A non-stationary time series, on the other hand, has one or more of these properties changing over time. A stationary time series is easier to model than a non-stationary time series.
ARMA (Autoregressive Moving Average) models are a class of statistical models for analyzing and forecasting time series data. ARMA models are fitted to time series data either by using maximum likelihood or by minimizing the sum of squares of the differences between the actual observations and those predicted by the model.
'''

import pandas as pd
import statsmodels.api as sm


def load_data(file_path):
    """Load time series data from a CSV file"""
    data = pd.read_csv(file_path, index_col=0, parse_dates=True)
    return data


def seasonal_decomposition(data, model='additive', freq=None):
    """Perform seasonal decomposition on a time series"""
    decomposition = sm.tsa.seasonal_decompose(data, model=model, freq=freq)
    return decomposition


def adf_test(data):
    """Perform Augmented Dickey-Fuller test on a time series"""
    result = sm.tsa.stattools.adfuller(data)
    return result


def arma_model(data, order=(1, 1)):
    """Fit an ARMA model to a time series"""
    model = sm.tsa.ARMA(data, order=order)
    results = model.fit()
    return results

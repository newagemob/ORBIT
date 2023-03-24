import pandas as pd
import numpy as np
import yfinance as yf
import statsmodels.api as sm
import matplotlib.pyplot as plt


def compute_log_returns(data):
    """
    Compute the log returns for a given DataFrame.

    Args:
        data (DataFrame): Historical stock data.

    Returns:
        DataFrame: DataFrame containing the log returns.
    """
    log_returns = np.log(data['Adj Close']).diff()
    return log_returns


def perform_regression_analysis(log_returns):
    """
    Perform regression analysis on the given log returns.

    Args:
        log_returns (DataFrame): DataFrame containing the log returns.

    Returns:
        Statsmodels OLS Results: Results of the regression analysis.
    """
    X = sm.add_constant(log_returns.shift())
    Y = log_returns
    model = sm.OLS(Y.dropna(), X.dropna())
    results = model.fit()
    return results


def plot_residuals(ticker, results):
    """
    Plot the residuals of the regression analysis.

    Args:
        ticker (str): Stock ticker symbol.
        results (Statsmodels OLS Results): Results of the regression analysis.
    """
    plt.figure()
    plt.plot(results.resid)
    plt.title('Residuals Plot for '+ ticker)


def plot_autocorrelation(ticker, log_returns):
    """
    Plot the autocorrelation function (ACF) and partial autocorrelation function (PACF) of the log returns.

    Args:
        ticker (str): Stock ticker symbol.
        log_returns (DataFrame): DataFrame containing the log returns.
    """
    acf = sm.tsa.stattools.acf(log_returns.dropna(), nlags=20)
    pacf = sm.tsa.stattools.pacf(log_returns.dropna(), nlags=20)

    plt.figure()
    plt.subplot(2, 1, 1)
    plt.stem(acf)
    plt.title('Autocorrelation Function (ACF) for '+ ticker)
    plt.subplot(2, 1, 2)
    plt.stem(pacf)
    plt.title('Partial Autocorrelation Function (PACF) for '+ ticker)
    plt.tight_layout()


def perform_quantitative_analysis(ticker):
    """
    Perform quantitative analysis on a given stock.

    Args:
        ticker (str): Stock ticker symbol.

    Returns:
        dict: Dictionary containing the analysis results.
    """
    # Download the historical data from Yahoo Finance
    data = yf.download(ticker, start='2010-01-01', end='2022-02-23')

    # Compute the log returns and store them in a new column
    data['Log Returns'] = compute_log_returns(data)

    # Perform regression analysis
    results = perform_regression_analysis(data['Log Returns'])

    # Plot the residuals to check for autocorrelation
    plot_residuals(ticker, results)

    # Plot the autocorrelation function (ACF) and partial autocorrelation function (PACF)
    plot_autocorrelation(ticker, data['Log Returns'])

    # Create dictionary containing the analysis results
    analysis_results = {
        'Ticker': ticker,
        'R-Squared': results.rsquared,
        'ADF Statistic': sm.tsa.stattools.adfuller(data['Log Returns'].dropna())[0],
        'ADF p-value': sm.tsa.stattools.adfuller(data['Log Returns'].dropna())[1]
    }

    return analysis_results


def perform_quantitative_analysis_batch(tickers):
    """
    Perform quantitative analysis on a list of stocks.

    Args:
        tickers (list): List of stock ticker symbols.

    Returns:
        DataFrame: DataFrame containing the analysis results.
    """
    
    analysis_results = []
    for ticker in tickers:
        analysis_result = perform_quantitative_analysis(ticker)
        analysis_results.append(analysis_result)

    analysis_results = pd.DataFrame(analysis_results)
    return analysis_results


def main():
    # Read in the list of S&P 500 stocks
    stocks = pd.read_csv('sp500.csv')

    # Perform quantitative analysis on a list of stocks
    analysis_results = perform_quantitative_analysis_batch(stocks['Ticker'][:5])

    # Print the analysis results
    print(analysis_results)


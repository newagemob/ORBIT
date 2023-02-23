import pandas as pd
import numpy as np
import yfinance as yf
import statsmodels.api as sm
import matplotlib.pyplot as plt

tickers = ['AAPL', 'MSFT', 'GOOG', 'AMZN']

# Define a function to perform the quantitative analysis for a given ticker symbol
def quantitative_analysis(ticker):
    # Download the historical data from Yahoo Finance
    data = yf.download(ticker, start='2010-01-01', end='2022-02-23')
    
    # Compute the log returns and store them in a new column
    data['Log Returns'] = np.log(data['Adj Close']).diff()
    
    # Regression analysis
    X = sm.add_constant(data['Log Returns'].shift())
    Y = data['Log Returns']
    model = sm.OLS(Y.dropna(), X.dropna())
    results = model.fit()
    
    # Plot the residuals to check for autocorrelation
    plt.figure()
    plt.plot(results.resid)
    plt.title('Residuals Plot for '+ ticker)
    
    # Time series analysis
    # Compute the autocorrelation function (ACF) and partial autocorrelation function (PACF) of the log returns
    acf = sm.tsa.stattools.acf(data['Log Returns'].dropna(), nlags=20)
    pacf = sm.tsa.stattools.pacf(data['Log Returns'].dropna(), nlags=20)
    
    # Plot the ACF and PACF
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.stem(acf)
    plt.title('Autocorrelation Function (ACF) for '+ ticker)
    plt.subplot(2, 1, 2)
    plt.stem(pacf)
    plt.title('Partial Autocorrelation Function (PACF) for '+ ticker)
    plt.tight_layout()

# Loop over the list of tickers and perform the quantitative analysis for each one
for ticker in tickers:
    quantitative_analysis(ticker)

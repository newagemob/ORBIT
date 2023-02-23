'''
Technical Analysis using moving averages, RSI, and Bollinger bands

Moving averages are a simple technical indicator that smooths out price data by creating a constantly updated average price.
RSI (Relative Strength Index) is a momentum indicator that measures the magnitude of recent price changes to evaluate overbought or oversold conditions in the price of a stock or other asset.
Bollinger bands are a technical analysis tool defined by a set of lines plotted two standard deviations (positively and negatively) away from a simple moving average (SMA) of the security's price, but can be adjusted to user preferences.

Both moving averages and Bollinger bands are trend-following indicators, which means that they are used to identify when the price of a stock is trending upward or downward.
'''

import pandas as pd
import yfinance as yf
import numpy as np
import ta

def technical_analysis(tickers):
    for i, ticker in enumerate(tickers):
        # Download stock data from Yahoo Finance
        data = yf.download(ticker, period='max', interval='1d')
        # Drop any rows with missing values
        data.dropna(inplace=True)

        # Calculate technical indicators using the 'ta' library
        data['SMA_20'] = ta.trend.sma_indicator(data['Close'], window=20)
        data['SMA_50'] = ta.trend.sma_indicator(data['Close'], window=50)
        data['EMA_20'] = ta.trend.ema_indicator(data['Close'], window=20)
        data['EMA_50'] = ta.trend.ema_indicator(data['Close'], window=50)
        data['RSI'] = ta.momentum.rsi(data['Close'], window=14)
        data['MACD'] = ta.trend.macd_diff(data['Close'], window_slow=26, window_fast=12, window_sign=9)

        # Add columns to indicate buy/sell signals
        data['Signal'] = 0.0
        data['Signal'] = np.where(data['SMA_20'] > data['SMA_50'], 1.0, 0.0)
        data['Signal'] = np.where(data['EMA_20'] > data['EMA_50'], 1.0, 0.0)
        data['Signal'] = np.where(data['RSI'] < 30, 1.0, 0.0)
        data['Signal'] = np.where(data['MACD'] > 0, 1.0, 0.0)

        # Calculate returns based on buy/sell signals
        data['BuyHold'] = data['Close'].pct_change()
        data['Strategy'] = data['BuyHold'] * data['Signal'].shift(1)

        # Calculate and print the strategy's overall returns
        strategy_returns = data['Strategy'].sum()
        print(f"{ticker}: Overall strategy returns = {strategy_returns:.2%}")

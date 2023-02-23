

import pandas as pd
import numpy as np
import datetime as dt

def out_of_sample(test_data, strategy_func):
    """
    Performs an out-of-sample test of a trading strategy using the given test data.

    Args:
    - test_data (pandas.DataFrame): A DataFrame containing the out-of-sample test data.
    - strategy_func (function): A function that takes in a DataFrame of historical prices and returns
                                a DataFrame of trading signals (BUY, SELL, HOLD) for each date.

    Returns:
    - results (pandas.DataFrame): A DataFrame containing the results of the out-of-sample test.
    """
    # Compute the trading signals using the historical data
    signals = strategy_func(test_data)
    
    # Compute the returns based on the trading signals
    test_data['Signal'] = signals
    test_data['Signal'].fillna(method='ffill', inplace=True)
    test_data['Return'] = test_data['Close'].pct_change() * test_data['Signal'].shift(1)
    
    # Compute the cumulative returns and other performance metrics
    test_data['Cumulative Return'] = (1 + test_data['Return']).cumprod()
    start_date = test_data.index[0]
    end_date = test_data.index[-1]
    total_return = (test_data['Cumulative Return'][-1] - 1) * 100
    cagr = (test_data['Cumulative Return'][-1] ** (365 / len(test_data)) - 1) * 100
    sharpe_ratio = np.sqrt(252) * test_data['Return'].mean() / test_data['Return'].std()
    
    # Construct the results DataFrame
    results = pd.DataFrame({'Start Date': [start_date],
                            'End Date': [end_date],
                            'Total Return (%)': [total_return],
                            'CAGR (%)': [cagr],
                            'Sharpe Ratio': [sharpe_ratio]})
    results.set_index('Start Date', inplace=True)
    
    return results

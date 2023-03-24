'''
This function takes a pandas DataFrame df containing the historical prices of a stock, along with several other parameters, and returns a DataFrame containing the trade signals and portfolio values, along with the Sharpe ratio.
'''

import pandas as pd
import numpy as np

def historical_simulation(df, window, cutoff, position_size):
    """
    A trading strategy function that implements the Historical Simulation method.

    Parameters:
    df (pandas.DataFrame): a DataFrame containing the historical prices of a stock
    window (int): the number of days to use for computing the historical returns
    cutoff (float): the quantile value to use as the cutoff for selecting trades
    position_size (float): the fraction of the portfolio to allocate to each trade

    Returns:
    pandas.DataFrame: a DataFrame containing the trade signals and portfolio values
    """
    # Compute the historical returns
    returns = df['Close'].pct_change()

    # Compute the historical VaR
    var = returns.rolling(window=window).quantile(cutoff)

    # Compute the trade signals
    signals = pd.DataFrame(index=df.index, columns=['Signal'])
    signals['Signal'] = np.where(returns.shift(-1) < var.shift(-1), 1, 0)

    # Compute the portfolio values
    portfolio = pd.DataFrame(index=df.index, columns=['Holdings', 'Cash', 'Total'])
    portfolio['Holdings'] = signals['Signal'] * position_size
    portfolio['Cash'] = -1 * portfolio['Holdings'] * df['Close']
    portfolio['Total'] = portfolio['Cash'].cumsum() + (portfolio['Holdings'] * df['Close'])

    # Compute the daily returns
    daily_returns = portfolio['Total'].pct_change()

    # Compute the Sharpe ratio
    sharpe_ratio = (np.sqrt(252) * daily_returns.mean()) / daily_returns.std()

    # Return the trade signals and portfolio values
    return pd.concat([signals, portfolio], axis=1), sharpe_ratio

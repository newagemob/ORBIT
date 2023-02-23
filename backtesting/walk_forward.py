'''
Walk Forward Analysis involves dividing historical data into multiple time periods, using each period to train a trading model, and then testing the model on a subsequent time period.

simulate the performance of the trading model on new data by periodically re-estimating the model's parameters and re-optimizing its settings based on the most recent historical data.
this helps to avoid the problem of overfitting, which occurs when a model performs well on historical data but fails to generalize to new data.
using a rolling window approach, walk-forward analysis allows for a more accurate assessment of the performance of a trading strategy in real-world conditions.
'''

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Tuple


def calculate_returns(prices: pd.Series) -> pd.Series:
    """Calculates the returns of a price series."""
    return prices.pct_change(1)


def calculate_strategy_returns(returns: pd.Series, signals: pd.Series) -> pd.Series:
    """Calculates the returns of a strategy given the signal series."""
    return returns * signals.shift(1)


def calculate_metrics(returns: pd.Series, benchmark_returns: pd.Series) -> Tuple[float, float, float, float]:
    """Calculates the Sharpe Ratio, Sortino Ratio, Maximum Drawdown, and Total Return of a series of returns."""
    excess_returns = returns - benchmark_returns
    avg_excess_return = excess_returns.mean()
    std_dev = excess_returns.std()
    sharpe_ratio = avg_excess_return / std_dev * np.sqrt(252)
    downside_returns = excess_returns[excess_returns < 0]
    avg_downside_return = downside_returns.mean()
    sortino_ratio = avg_excess_return / std_dev * np.sqrt(252)
    cumulative_returns = (1 + returns).cumprod()
    max_drawdown = (cumulative_returns.cummax() - cumulative_returns).max()
    total_return = cumulative_returns[-1] - 1
    return sharpe_ratio, sortino_ratio, max_drawdown, total_return


def walk_forward_analysis(prices: pd.DataFrame, strategy_function, window_size: int, step_size: int) -> pd.DataFrame:
    """Performs walk-forward analysis on a DataFrame of prices given a strategy function."""
    signals = pd.Series(index=prices.index)
    returns = pd.Series(index=prices.index)
    sharpe_ratios = []
    sortino_ratios = []
    max_drawdowns = []
    total_returns = []
    start_date = prices.index[0]
    end_date = prices.index[-1]
    current_date = start_date + timedelta(days=window_size)
    while current_date < end_date:
        train_prices = prices.loc[start_date:current_date]
        test_prices = prices.loc[current_date + timedelta(days=1):current_date + timedelta(days=step_size)]
        train_returns = calculate_returns(train_prices['Close'])
        test_returns = calculate_returns(test_prices['Close'])
        signals.loc[test_returns.index] = strategy_function(train_prices, test_prices)
        returns.loc[test_returns.index] = calculate_strategy_returns(test_returns, signals.loc[test_returns.index])
        benchmark_returns = calculate_returns(test_prices['Close'])
        sharpe_ratio, sortino_ratio, max_drawdown, total_return = calculate_metrics(returns.loc[test_returns.index], benchmark_returns)
        sharpe_ratios.append(sharpe_ratio)
        sortino_ratios.append(sortino_ratio)
        max_drawdowns.append(max_drawdown)
        total_returns.append(total_return)
        current_date = current_date + timedelta(days=step_size)
        start_date = start_date + timedelta(days=step_size)
    results = pd.DataFrame({'Sharpe Ratio': sharpe_ratios,
                            'Sortino Ratio': sortino_ratios,
                            'Max Drawdown': max_drawdowns,
                            'Total Return': total_returns},
                            index=signals.index[window_size:])
    return results

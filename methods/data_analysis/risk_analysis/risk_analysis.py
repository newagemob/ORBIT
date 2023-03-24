from typing import Tuple
import pandas as pd
import numpy as np

def historical_var(returns: pd.Series, alpha: float) -> float:
    """
    Calculate Value at Risk (VaR) using Historical Simulation
    :param returns: pandas series of asset returns
    :param alpha: confidence level
    :return: VaR
    """
    return -np.percentile(returns, alpha)


def stop_loss(price_data: pd.DataFrame, stop_loss_percent: float) -> pd.Series:
    """
    Implement a stop loss on price data
    :param price_data: pandas dataframe of price data
    :param stop_loss_percent: percentage stop loss
    :return: pandas dataframe with stop loss applied
    """
    max_price = price_data['Adj Close'].cummax()
    stop_loss_price = max_price * (1 - stop_loss_percent)
    return pd.concat([price_data['Adj Close'], stop_loss_price], axis=1).min(axis=1)


def risk_management(stock_data: pd.DataFrame, alpha: float, stop_loss_percent: float) -> Tuple[pd.DataFrame, float]:
    """
    Perform risk management analysis on a stock using VaR and stop loss
    :param stock_data: pandas dataframe of stock price data
    :param alpha: confidence level for VaR calculation
    :param stop_loss_percent: percentage stop loss
    :return: tuple containing pandas dataframe with stop loss applied and VaR value
    """
    returns = stock_data['Adj Close'].pct_change().dropna()
    var = historical_var(returns, alpha)
    stop_loss_data = stop_loss(stock_data, stop_loss_percent)
    result_df = pd.concat([stop_loss_data, pd.Series([var] * len(stock_data.index))], axis=1, keys=['Adj Close', 'VaR'])
    return result_df, var
publicProcedure
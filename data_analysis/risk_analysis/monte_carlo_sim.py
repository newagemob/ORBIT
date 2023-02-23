'''
Monte Carlo simulation is a method of generating a large number of random samples in order to obtain numerical results. In stock market analysis, Monte Carlo simulation can be used to model the behavior of a stock over time based on its past performance and statistical trends. By simulating many possible outcomes, we can estimate the likelihood of various scenarios, such as the likelihood of a stock's price reaching a certain level or the likelihood of a certain rate of return.
'''

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

def monte_carlo(ticker_list, days, simulations):
    '''
    Perform Monte Carlo simulation on a list of stock tickers.

    Parameters:
        ticker_list (list): A list of stock tickers.
        days (int): Number of days to simulate.
        simulations (int): Number of simulations to perform.

    Returns:
        dict: A dictionary containing the simulation results for each stock ticker.
    '''

    # Initialize dictionary to store simulation results for each stock ticker
    results = {}

    for i, ticker in enumerate(ticker_list):
        # Download data from Yahoo Finance
        data = yf.download(ticker, period="max")

        # Calculate daily returns
        daily_returns = data["Close"].pct_change()

        # Calculate mean and standard deviation of daily returns
        mean = daily_returns.mean()
        std = daily_returns.std()

        # Initialize empty array to store results
        simulations_arr = np.zeros((days, simulations))

        # Perform simulations
        for j in range(simulations):
            # Calculate the initial price
            price = data["Close"].iloc[-1]

            # Simulate price changes for the specified number of days
            for k in range(days):
                price = price * np.exp((mean - 0.5 * std**2) + std * np.random.normal())
                simulations_arr[k, j] = price

        # Store simulation results for the current stock ticker
        results[ticker] = simulations_arr

        # Generate report for the current stock ticker
        plt.figure(figsize=(10, 6))
        plt.title(f"{ticker} Monte Carlo Simulation")
        plt.xlabel("Day")
        plt.ylabel("Price")
        plt.plot(simulations_arr)
        plt.savefig(f"{ticker}_monte_carlo_simulation.png")
        plt.close()

    return results

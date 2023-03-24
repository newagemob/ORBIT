'''
This script takes in a DataFrame of daily returns, the number of simulations to run, and the initial portfolio value

It then calculates the mean and standard deviation of the daily returns, generates a random normal distribution of daily returns, and calculates the cumulative returns for each simulation. It also calculates the 5th, 50th, and 95th percentiles for each day in the simulation and creates a DataFrame of simulation results. Finally, it plots the simulation results and returns the simulation results DataFrame.

Using this script requires a generatede DataFrame of daily returns from the ORBIT pipeline's data collection and processing outputs.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run_monte_carlo_simulation(returns_df, num_simulations, initial_portfolio_value):
    # Calculate mean and standard deviation of daily returns
    daily_returns = returns_df.pct_change()
    mu = daily_returns.mean().values[0]
    sigma = daily_returns.std().values[0]

    # Generate random normal distribution of daily returns
    sim_returns = np.random.normal(mu, sigma, size=(returns_df.shape[0], num_simulations))

    # Calculate cumulative returns for each simulation
    sim_cumulative_returns = (1 + sim_returns).cumprod(axis=0) * initial_portfolio_value

    # Calculate percentiles for each day in the simulation
    percentiles = np.percentile(sim_cumulative_returns, [5, 50, 95], axis=1)

    # Create dataframe of simulation results
    simulation_results = pd.DataFrame({
        '5th Percentile': percentiles[0],
        '50th Percentile': percentiles[1],
        '95th Percentile': percentiles[2]
    }, index=returns_df.index)

    # Plot simulation results
    plt.figure(figsize=(10, 5))
    plt.plot(simulation_results.index, simulation_results['50th Percentile'], color='blue', label='Median')
    plt.fill_between(simulation_results.index, simulation_results['5th Percentile'], simulation_results['95th Percentile'], color='gray', alpha=0.5, label='5th-95th Percentile')
    plt.legend(loc='upper left')
    plt.xlabel('Date')
    plt.ylabel('Portfolio Value')
    plt.title('Monte Carlo Simulation')
    plt.show()

    return simulation_results

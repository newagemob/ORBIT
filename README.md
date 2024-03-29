# 🛰️ ORBIT

***Optimized Risk-Based Intelligence Trading***

# Order of Operations

Steps to take for every trade:

* Data collection: Collect data from exchanges, news outlets, social media platforms, and economic calendars. This could involve scraping websites, accessing APIs, or downloading data from databases.

* Stock market data analysis: You will need to use libraries such as Pandas and NumPy to import and analyze stock market data. Pandas is a library used for data manipulation and analysis, while NumPy is a library used for mathematical and statistical operations.

* Data visualization: You will also need to use libraries such as Matplotlib and Seaborn to visualize stock market data and gain insights into trends and patterns.

* Statistical modeling: You will need to understand statistical concepts such as mean, standard deviation, correlation, and regression to analyze stock market data and build trading models.

* Backtesting: This involves testing the trading strategy using historical stock market data to see how it would have performed in the past. You can use libraries such as Backtrader or PyAlgoTrade to backtest the strategies.

* Trading algorithms: You will need to implement the trading strategies, including defining entry and exit conditions, managing risk, and executing trades.

## Implementation

* Determine the goal and scope of the analysis, such as identifying potential trading opportunities, assessing market trends, or optimizing trading strategies.

* Identify and obtain relevant data sources, such as stock prices, financial reports, and news articles. This could involve scraping websites, accessing APIs, or downloading data from databases.

* Preprocess and clean the data to remove any errors, inconsistencies, or missing values. This step could include converting data types, normalizing values, and filling in missing data.

* Conduct exploratory data analysis (EDA) to gain insights into the data and identify any patterns or relationships. This could involve visualizing the data using charts, graphs, and other tools.

* Apply statistical and machine learning techniques to the data to develop trading algorithms. This could include regression analysis, time series forecasting, and clustering.

* Backtest the trading algorithms using historical data to assess their performance and identify any issues or limitations. This step could involve simulating trades and analyzing the results.

* Refine and optimize the trading algorithms based on the results of the backtesting. This could involve tweaking the parameters of the algorithms or incorporating new data sources.

* Implement the trading algorithms in a live trading environment, such as a trading platform or API. This step requires integrating the algorithms with the trading system and monitoring their performance in real-time.

* Monitor and evaluate the performance of the trading algorithms over time. This could involve analyzing trade data, adjusting the algorithms based on market conditions, and identifying areas for improvement.

* Continuously refine and improve the trading algorithms based on ongoing analysis and feedback. This step requires staying up-to-date with market trends and adapting to changing conditions.

The data structure for OpenLiquid's algorithmic trading pipeline could include the following components:

Market Data: Raw data from different sources such as stock exchanges, news outlets, social media platforms, and economic calendars.

Preprocessing Pipeline: This pipeline will transform the raw market data into features that can be used by machine learning models. This process will include the following steps:

a. Data Cleaning: Removing missing or irrelevant data.

b. Feature Engineering: Creating new features that might be useful to the model.

c. Feature Scaling: Normalizing the data so that all features have the same scale.

d. Feature Selection: Selecting only the relevant features for the model.

Machine Learning Models: This component will contain different machine learning models, such as regression, clustering, and classification algorithms, to predict market trends and trading signals.

Trading Strategies: Based on the predictions of the machine learning models, trading strategies will be designed to execute trades in the market. These strategies could be simple or complex, such as mean-reversion, momentum, or trend-following.

Order Management System: This system will receive the trading signals from the trading strategies and execute the trades in the market. It will also manage the orders and handle the order book.

Portfolio Management System: This system will manage the portfolio of the trades executed by the order management system. It will analyze the performance of the portfolio and adjust the trading strategies based on the market conditions.

Risk Management System: This system will manage the risk associated with the trades executed by the order management system. It will monitor the risk factors such as market volatility, liquidity, and counterparty risk, and adjust the trading strategies to minimize the risk.

Reporting and Analysis System: This system will provide the reports and analysis of the trading performance. It will generate the daily, weekly, and monthly reports, and provide the insights and recommendations for the portfolio management system.

The input data for the OpenLiquid's algorithmic trading pipeline will be raw market data from different sources such as stock exchanges, news outlets, social media platforms, and economic calendars. The output of the pipeline will be trading signals generated by the trading strategies and executed by the order management system. The pipeline will also provide the reports and analysis of the trading performance generated by the reporting and analysis system.


# Getting Started 🚀

## Prerequisites

* [Conda Environment Manager](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
* ^[Python 3.9](https://www.python.org/downloads/)

## Installation

1. Clone the repo

```sh
git clone
```

2. Install Conda packages

```sh
conda env create -f environment.yml
```

3. Activate the Conda environment

```sh
conda activate orbit
```

4. Install Python packages

```sh
pip install -r requirements.txt && pip install -e ./methods
```

## Usage

1. Activate the Conda environment

```sh
conda activate orbit
```

2. Run the main script. This will start the ORBIT agent, walking you through the configuration process, and then running the pipeline.

```sh
python orbit-agent.py
```

# How ORBIT Works

ORBIT needs to know a few things before it can start working for you. Modify the `config.yml` file to specify the following information about your trading strategy:

---
* How much capital do you have to invest? This includes the amount of capital, the currency of the capital, and the exchange rate of the capital. ***Required***
* What is your risk tolerance? This includes the maximum amount of risk, the maximum amount of loss, and the maximum amount of drawdown. ***Required***
* How often should the pipeline run? This includes the frequency of trades, the frequency of model updates, and how often live data should be collected. ***Required***
* What is your time horizon? This includes simulation time, maximum time to trade, maximum time to hold a position, etc. ***Note:*** *The default time horizon is 1 year.*
* What is your preferred data source? This includes the type of data, the parameters of the data, and the data rules. ***Note:*** *Default data sources are provided if none are specified.*
* What is your preferred trading platform? This includes the type of platform, the parameters of the platform, and the platform rules. ***Note:*** *Default platforms are provided if none are specified.*
* What is your preferred trading model? This includes the type of model, the parameters of the model, and the model rules. ***Note:*** *Default models are provided if none are specified.*
---


```py
# This is the setup script for the qsforex package. Use this to initialize the packages and modules in the qsforex directory.

from setuptools import setup, find_packages

setup(
    name='qsforex',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
      'ipython',
      'matplotlib',
      'mock',
      'nose',
      'numpy',
      'pandas',
      'pyparsing',
      'python-dateutil',
      'pytz',
      'requests',
      'scikit-learn',
      'scipy',
      'seaborn',
      'six',
      'urllib3',
    ]
)
```

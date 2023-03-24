# Daily Operation Procedures

## Overview

The goal of ORBIT (Optimized Risk Base Intelligence Trading) is to provide a simple, easy to use, and reliable system to consitently reproduce profitable trades. Using the method outlined in the [Trading Strategy Overview](https://github.com/newagemob/openliquid-client/blob/main/src/pages/docs/structure/markdown_docs/00_OpenLiquid_Strategy_Overview.md) document, ORBIT will execute trades on a daily basis.

Ideally, this agent will be able to run in a headless environment, and will be able to execute trades during the entire trading day (9:30am - 4:00pm EST) for the [US stock market](#US_Stocks), and the entire day (12:00am - 11:00pm CST) for the [crypto market](#Crypto).

This document outlines the steps necessary to generate analysis data, perform statistical modeling, backtest the models, and execute the trades.

# US Stocks

## Daily Steps

### ***NOTE:*** *Currently only running on the SP500*
### 1. Generate Analysis Data

Use `_pipelines.pipeline_SP500.py` script to generate the specified analysis data. CURRENTLY INCLUDES `data_collection.scrape_stock_data.py` to generate the analysis data from SP500. This script will generate `sp500_analysis.csv` - Contains Company Name, Ticker Symbol, Weight in SP500, Price of Stock, Change in Price, and Percent Change in Price.

With the analysis data generated, we can now generate both the human readable and machine readable data.

### 2. Generate Human Readable Data

Use `data_analysis.human_summary.py` to generate the human readable data from the analysis data. This script will generate `sp500_human_summary.csv` - Contains Top 10 Gainers, Top 10 Losers, and Top 10 Most Active, then shows their historical data - 1 Day, 5 Day, 1 Month, 3 Month, 6 Month, 1 Year, 5 Year, and 10 Year (if available).

### 3. Generate Machine Readable Data

Use `data_analysis.machine_learning.model_data.py` to generate the machine readable data from the analysis data. This script will generate `sp500_model_data.csv` - Contains the data necessary to generate the statistical models. The model data will be shaped to best fit the statistical models required to generate the trading signals.

### 4. Generate Statistical Models

### 5. Backtest Models

### 6. Execute Trades

# Crypto

## Daily Steps


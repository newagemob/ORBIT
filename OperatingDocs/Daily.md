# Daily Operation Procedures

## Overview

The goal of ORBIT (Optimized Risk Base Intelligence Trading) is to provide a simple, easy to use, and reliable system to consitently reproduce profitable trades. Using the method outlined in the [Trading Strategy Overview](https://github.com/newagemob/openliquid-client/blob/main/src/pages/docs/structure/markdown_docs/00_OpenLiquid_Strategy_Overview.md) document, ORBIT will execute trades on a daily basis. This document outlines the steps necessary to generate analysis data, perform statistical modeling, backtest the models, and execute the trades. Each step is 

## Daily Steps

### 1. Generate Analysis Data

Use `generate_analysis_data.py` script to generate the specified analysis data. FOR NOW, use `scrape_stock_data.py` to generate the analysis data from SP500 and NASDAQ stocks.

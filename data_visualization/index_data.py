import pandas as pd
import yfinance as yf
import re
import matplotlib.pyplot as plt
from progress.bar import ChargingBar

def get_index_data(filename: str, duration: str):
    # read in the index list and select the top `num_stocks` by weight
    index_data = pd.read_csv(filename)
    # count the number of rows in the DataFrame
    num_stocks = len(index_data.index)
    index_top = index_data.nlargest(num_stocks, "Weight")

    # get the stock data from Yahoo Finance
    tickers = index_top["Symbol"].tolist()
    bar = ChargingBar(f"Getting stock prices ({duration})", max=len(tickers))

    current_stock_data = []
    annual_returns = []
    weekly_returns = []

    for ticker in tickers:
        if (re.search(r"\.", ticker) or re.search(r"\-", ticker)):
            current_stock_data.append(0)
            annual_returns.append(0)
            weekly_returns.append(0)
        else:
            stock = yf.Ticker(ticker)
            hist = stock.history(period=duration)
            current_stock_data.append(hist["Close"].tolist()[0])

            hist = stock.history(period="1y")
            current_price = hist["Close"].tolist()[0]
            one_year_ago_price = hist["Close"].tolist()[-1]
            stock_return = current_price / one_year_ago_price - 1
            annual_returns.append(stock_return)

            hist = stock.history(period="1wk")
            current_price = hist["Close"].tolist()[0]
            one_week_ago_price = hist["Close"].tolist()[-1]
            stock_return = current_price / one_week_ago_price - 1
            weekly_returns.append(stock_return)

        bar.next()

    bar.finish()

    # add the stock data and calculated returns to the DataFrame
    index_top["YFi Stock Price"] = current_stock_data
    index_top["Total Value"] = index_top["YFi Stock Price"] * index_top["Weight"]
    total_value = index_top["Total Value"].sum()
    index_top["Percentage"] = index_top["Total Value"] / total_value
    index_top["Annual Return"] = annual_returns
    index_top["Weekly Return"] = weekly_returns

    # plot the top performers and losers
    top10 = index_top.nlargest(10, "Annual Return")
    top10.plot.bar(x="Symbol", y="Annual Return", rot=0)
    plt.show()
    plt.pause(5)
    plt.close()

    top10.plot.bar(x="Symbol", y="Weekly Return", rot=0)
    plt.show()

    bottom10 = index_top.nsmallest(10, "Annual Return")
    bottom10.plot.bar(x="Symbol", y="Annual Return", rot=0)
    plt.show()

    bottom10.plot.bar(x="Symbol", y="Weekly Return", rot=0)
    plt.show()

# Equal-Weight S&P 500 Index Fund

import yfinance as yf
import pandas as pd
import xlsxwriter
import matplotlib.pyplot as plt
import re
from progress.bar import ChargingBar


def get_sp100(filename: str, num_stocks: int, duration: str):
    # read in the S&P 500 list and select the top `num_stocks` by weight
    sp500 = pd.read_csv(filename)
    sp100 = sp500.nlargest(num_stocks, "Weight")

    # get the stock data from Yahoo Finance
    tickers = sp100["Symbol"].tolist()
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
    sp100["YFi Stock Price"] = current_stock_data
    sp100["Total Value"] = sp100["YFi Stock Price"] * sp100["Weight"]
    total_value = sp100["Total Value"].sum()
    sp100["Percentage"] = sp100["Total Value"] / total_value
    sp100["Annual Return"] = annual_returns
    sp100["Weekly Return"] = weekly_returns

    # output the data to files
    writer = pd.ExcelWriter("sp100.xlsx", engine="xlsxwriter")
    sp100.to_excel(writer, index=False, sheet_name="SP100")
    writer.save()

    sp100.to_csv("./output/sp100.csv", index=False)

    # plot the top performers and losers
    top10 = sp100.nlargest(10, "Annual Return")
    top10.plot.bar(x="Symbol", y="Annual Return", rot=0)
    plt.show()
    plt.pause(5)
    plt.close()

    top10.plot.bar(x="Symbol", y="Weekly Return", rot=0)
    plt.show()

    bottom10 = sp100.nsmallest(10, "Annual Return")
    bottom10.plot.bar(x="Symbol", y="Annual Return", rot=0)
    plt.show()

    bottom10.plot.bar(x="Symbol", y="Weekly Return", rot=0)
    plt.show()

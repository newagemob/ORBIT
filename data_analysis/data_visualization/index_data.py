import pandas as pd
import yfinance as yf
import re
import matplotlib.pyplot as plt
from progress.bar import ChargingBar
import time

def get_index_data(filename: str, duration: str):
    index_data = pd.read_csv(filename)
    num_stocks = len(index_data) # count rows in the DataFrame
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

    # date for the output file
    date = time.strftime("%Y-%m-%d")
    # strip filename for the output file
    index_name = filename.split("/")[-1].split(".")[0]

    # plot the top performers and losers
    top10 = index_top.nlargest(10, "Annual Return") # top 10 stocks in list by annual return
    top10.plot.bar(x="Symbol", y="Annual Return", rot=0)
    # save the plot to a file
    plt.savefig(f"~/Developer/openliquid-capital/orbit/data_visualization/output/{index_name}_{date}_top10_annual.png")

    top10.plot.bar(x="Symbol", y="Weekly Return", rot=0) # top 10 stocks in list by weekly return
    plt.savefig(f"~/Developer/openliquid-capital/orbit/data_visualization/output/{index_name}_{date}_top10_weekly.png")

    bottom10 = index_top.nsmallest(10, "Annual Return") # bottom 10 stocks in list by annual return
    bottom10.plot.bar(x="Symbol", y="Annual Return", rot=0)
    plt.savefig(f"~/Developer/openliquid-capital/orbit/data_visualization/output/{index_name}_{date}_bottom10_annual.png")

    bottom10.plot.bar(x="Symbol", y="Weekly Return", rot=0) # bottom 10 stocks in list by weekly return
    plt.savefig(f"~/Developer/openliquid-capital/orbit/data_visualization/output/{index_name}_{date}_bottom10_weekly.png")

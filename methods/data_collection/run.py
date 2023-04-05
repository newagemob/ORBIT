'''
Current Funds / Stocks: S&P 500

This is the first step in the ORBIT pipeline. This script scrapes the specified companies from data_collection.scrape_stock_data and puts them into a CSV file in data_collection/output/{specified_stocks}_{date}.csv

This script is currently only running on S&P 500 stocks, but can be easily modified to run on any other stock or fund by changing the specified_stocks variable.
'''

import methods.data_collection.scrape_stock_data as scrape_stock_data
from methods.data_collection.scrape_historical_stocks import main as scrape_historical_stocks

# TODO: get these from `config.yaml`
funds = {
    "sp500": scrape_stock_data.scrape_sp500_stocks_today(),
}

stocks = {
    "aapl": scrape_stock_data.scrape_stock_symbol("AAPL"),
    "msft": scrape_stock_data.scrape_stock_symbol("MSFT"),
    "amzn": scrape_stock_data.scrape_stock_symbol("AMZN"),
    "googl": scrape_stock_data.scrape_stock_symbol("GOOGL"),
    "nvda": scrape_stock_data.scrape_stock_symbol("NVDA"),
}

# historical_funds = {
#     "sp500": scrape_historical_stocks(),
# }

# historical_stocks = {
#     "aapl": scrape_historical_stocks(),
#     "msft": scrape_historical_stocks(),
#     "amzn": scrape_historical_stocks(),
#     "googl": scrape_historical_stocks(),
#     "nvda": scrape_historical_stocks(),
# }

class DataCollection:
    def __init__(self, fund: str, stocks: list):
        self.fund = fund
        self.stocks = stocks
        # self.historical_funds = historical_funds
        # self.historical_stocks = historical_stocks

    def run(self):
        if self.fund in funds:
            funds[self.fund]()
            return
        elif self.stocks in stocks:
            stocks[self.stocks]()
        else:
            raise ValueError(f"Fund {self.fund or self.stocks} not found. Please check the available funds and stocks in the config.yaml file.")
      

if __name__ == "__main__":
  data_collection = DataCollection("sp500", [])
  data_collection.run()

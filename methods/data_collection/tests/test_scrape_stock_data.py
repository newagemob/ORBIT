from methods.data_collection.scrape_stock_data import scrape_sp500_stocks_today, scrape_historical_sp500_stocks, scrape_stock_symbol


def main():
    scrape_sp500_stocks_today()
    # scrape_historical_sp500_stocks("2021-01-01", "2021-01-31")
    # scrape_stock_symbol("AAPL")

if __name__ == "__main__":
    main()

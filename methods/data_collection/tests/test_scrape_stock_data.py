from methods.data_collection.scrape_stock_data import scrape_sp500_stocks_today, scrape_stock_symbol


def main():
    scrape_sp500_stocks_today()
    # scrape_stock_symbol("AAPL")

if __name__ == "__main__":
    main()

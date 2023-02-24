import requests
import pandas as pd


def scrape_sp500_stocks(stocks_csv_path: str) -> pd.DataFrame:
    """
    Reads in a CSV file containing a list of S&P 500 stocks and returns a DataFrame.
    
    Parameters:
    stocks_csv_path (str): The file path to the CSV file containing the list of S&P 500 stocks.
    
    Returns:
    pd.DataFrame: A DataFrame containing the list of S&P 500 stocks.
    """
    slickcharts_url = "https://www.slickcharts.com/sp500"
    page = requests.get(slickcharts_url)
    df = pd.read_html(requests.get(slickcharts_url ,headers={'User-agent': 'Mozilla/5.0'}).text)[0]
    df.to_csv(stocks_csv_path, index=False)
    return df


def scrape_nasdaq_stocks(stocks_csv_path: str) -> pd.DataFrame:
    """
    Reads in a CSV file containing a list of NASDAQ stocks and returns a DataFrame.
    
    Parameters:
    stocks_csv_path (str): The file path to the CSV file containing the list of NASDAQ stocks.
    
    Returns:
    pd.DataFrame: A DataFrame containing the list of NASDAQ stocks.
    """
    nasdaq_url = "https://www.nasdaq.com/market-activity/stocks/screener"
    page = requests.get(nasdaq_url)
    df = pd.read_html(requests.get(nasdaq_url ,headers={'User-agent': 'Mozilla/5.0'}).text)[0]
    df.to_csv(stocks_csv_path, index=False)
    return df

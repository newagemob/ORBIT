import requests
import pandas as pd
from bs4 import BeautifulSoup


def scrape_sp500_stocks() -> pd.DataFrame:
    """
    Scrapes the list of S&P 500 stocks from slickcharts.com and returns a DataFrame.
    
    Returns:
    pd.DataFrame: A DataFrame containing the list of S&P 500 stocks.
    """
    url = "https://www.slickcharts.com/sp500"
    try:
        response = requests.get(url ,headers={'User-agent': 'Mozilla/5.0'})
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        return None
    
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find_all("table")[0] # find the first table
    df = pd.read_html(str(table))[0] # read the HTML table into a DataFrame
    df.to_csv("./output/sp500_stocks.csv", index=False) # save to CSV
    return df


def scrape_nasdaq_stocks() -> pd.DataFrame:
    """
    Scrapes the list of NASDAQ stocks from nasdaq.com and returns a DataFrame.
    
    Returns:
    pd.DataFrame: A DataFrame containing the list of NASDAQ stocks.
    """
    url = "https://www.nasdaq.com/market-activity/stocks/screener"
    try:
        response = requests.get(url ,headers={'User-agent': 'Mozilla/5.0'})
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        return None
    
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find_all("table")[0]
    df = pd.read_html(str(table))[0]
    df.to_csv("./output/nasdaq_stocks.csv", index=False)
    return df

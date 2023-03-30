import requests
import pandas as pd
from bs4 import BeautifulSoup
from pathlib import Path
import datetime
from operator import itemgetter
import tqdm
# TODO: import the openbb package -- docs say I need a Windows machine to install it, but I'm going to try with my Debian machine
# from openbb_terminal.sdk import openbb

project_dir = Path(__file__).resolve().parents[3]

def scrape_sp500_stocks_today() -> pd.DataFrame:
    """
    Scrapes the list of S&P 500 stocks from slickcharts.com and returns a DataFrame.
    
    Returns:
    pd.DataFrame: A DataFrame containing the list of S&P 500 stocks.
    """

    # Slickcharts
    def slickcharts_sp500_stocks() -> pd.DataFrame:
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
        df_slickcharts = pd.read_html(str(table))[0] # read the HTML table  into a DataFrame
        # add the date to the last column of the DataFrame
        df_slickcharts['date'] = pd.Timestamp.today().strftime('%Y-%m-%d')

        for index, row in tqdm.tqdm(df_slickcharts.iterrows(),  total=df_slickcharts.shape[0]):
            symbol_url = f"https://slickcharts.com/symbol/{row['Symbol']}"

            '''
                Price	158.29	P/E (Trailing)	27.00
                Change	-0.64	P/E (Forward)	24.05
                Change %	-0.40%	EPS (Trailing)	5.89
                Prev Close	158.93	EPS (Forward)	6.61
                Volume	663,292	Dividend Yield	0.58%
                Market Cap	2528.37B	Dividend	0.92
            '''

            try:
                response = requests.get(symbol_url ,headers={'User-agent':  'Mozilla/5.0'})
                response.raise_for_status()
            except requests.exceptions.HTTPError as err:
                print(err)
                return None

            soup = BeautifulSoup(response.content, "html.parser")
            table = soup.find_all("table")[0] # find the first table
            th = table.find_all('th')
            headers = [h.text for h in th]
            td = table.find_all('td')
            data = [d.text for d in td]
            # get the index of the table header for each piece of data
            volume_index = headers.index('Volume')
            eps_trailing = headers.index('EPS (Trailing)')
            eps_forward = headers.index('EPS (Forward)')
            pe_trailing = headers.index('P/E (Trailing)')
            pe_forward = headers.index('P/E (Forward)')
            dividend_yield_index = headers.index('Dividend Yield')
            market_cap_index = headers.index('Market Cap')

            # add the data to the DataFrame
            df_slickcharts.at[index, 'Volume'] = data[volume_index]
            df_slickcharts.at[index, 'EPS (Trailing)'] = data[eps_trailing]
            df_slickcharts.at[index, 'EPS (Forward)'] = data[eps_forward]
            df_slickcharts.at[index, 'P/E (Trailing)'] = data[pe_trailing]
            df_slickcharts.at[index, 'P/E (Forward)'] = data[pe_forward]
            df_slickcharts.at[index, 'Dividend Yield'] = data   [dividend_yield_index]
            df_slickcharts.at[index, 'Market Cap'] = data[market_cap_index]

        df_slickcharts.to_csv(f"{project_dir}/orbit/methods/data_collection/output/SP500/slickcharts_sp500_stocks_{pd.Timestamp.today().strftime('%Y-%m-%d')}.csv", index=False)
        
        return df_slickcharts
    df_slickcharts = slickcharts_sp500_stocks()
    
    # Yahoo
    # use scrape_stock_symbol to get secondary data for each stock - used for further analysis, arbitrage, verifying stock data, etc. batch process this
    def yahoo_sp500_stocks() -> pd.DataFrame:
        """
        Scrapes the list of S&P 500 stocks from yahoo.com and returns a DataFrame.
        
        Returns:
        pd.DataFrame: A DataFrame containing the list of S&P 500 stocks.
        """
        
        df_yahoo = pd.DataFrame()

        for index, row in tqdm.tqdm(df_slickcharts.iterrows(),  total=df_slickcharts.shape[0]):
            # get headers and data returned from the scrape_stock_symbol    function
            stock_data = scrape_stock_symbol(row['Symbol'])
            symbol = stock_data[0]
            headers = stock_data[1]
            data = stock_data[2]
            # write the data to the DataFrame
            df_yahoo.at[index, 'Symbol'] = symbol
            for i in range(len(headers)):
                df_yahoo.at[index, headers[i]] = data[i]

        df_yahoo.to_csv(f"{project_dir}/orbit/methods/data_collection/output/SP500/yahoo_sp500_stocks_{pd.Timestamp.today().strftime('%Y-%m-%d')}.csv", index=False)

        return df_yahoo

    df_yahoo = yahoo_sp500_stocks()


def scrape_stock_symbol(symbol: str) -> pd.DataFrame:
    """Scrapes the stock's page on yahoo finance and returns a DataFrame.

    Args:
        symbol (str): The stock's ticker symbol.

    Returns:
        pd.DataFrame: A DataFrame containing the stock's information.
    """
    url = f"https://finance.yahoo.com/quote/{symbol}"
    try:
        response = requests.get(url ,headers={'User-agent': 'Mozilla/5.0'})
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        return None
    
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find_all("table")[0]
    # get table headers and data
    # the tr has two td elements, the first is the header and the second is the data
    tr = table.find_all('tr')
    headers = [t.find_all('td')[0].text for t in tr]
    data = [t.find_all('td')[1].text for t in tr]
    stock_symbol = symbol

    df = pd.DataFrame(data, index=headers, columns=[symbol])

    return symbol, headers, data

# Equal-Weight S&P 500 Index Fund

import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math

from typing import List

def get_sp500_stocks(stocks_csv_path: str) -> pd.DataFrame:
    """
    Reads in a CSV file containing a list of S&P 500 stocks and returns a DataFrame.
    
    Parameters:
    stocks_csv_path (str): The file path to the CSV file containing the list of S&P 500 stocks.
    
    Returns:
    pd.DataFrame: A DataFrame containing the list of S&P 500 stocks.
    """
    return pd.read_csv(stocks_csv_path)

def get_market_cap_and_price(symbol: str, api_key: str) -> tuple[float, float]:
    """
    Retrieves the market capitalization and price for a given stock symbol using the IEX Cloud API.
    
    Parameters:
    symbol (str): The stock symbol to retrieve data for.
    api_key (str): The API key to use when making the API request.
    
    Returns:
    tuple: A tuple containing the market capitalization and price for the given stock symbol.
    """
    api_url = f'https://cloud.iexapis.com/stable/stock/{symbol}/quote/?token={api_key}'
    data = requests.get(api_url).json()
    price = data['latestPrice']
    market_cap = data['marketCap'] / 1000000000
    
    return market_cap, price

def get_stock_data(stocks: pd.DataFrame, api_key: str) -> pd.DataFrame:
    """
    Retrieves the market capitalization and price for a list of stocks using the IEX Cloud API.
    
    Parameters:
    stocks (pd.DataFrame): A DataFrame containing the list of stocks to retrieve data for.
    api_key (str): The API key to use when making the API requests.
    
    Returns:
    pd.DataFrame: A DataFrame containing the market capitalization and price for each stock in the list.
    """
    csv_columns = ['Ticker', 'Stock Price', 'Market Capitalization']
    final_dataframe = pd.DataFrame(columns=csv_columns)

    symbol_groups = [stocks['Ticker'][i:i+100] for i in range(0, len(stocks), 100)]
    symbol_strings = [','.join(group) for group in symbol_groups]

    for symbol_string in symbol_strings:
        batch_api_call_url = f'https://cloud.iexapis.com/stable/stock/market/batch?symbols={symbol_string}&types=quote&token={api_key}'
        data = requests.get(batch_api_call_url).json()
        for symbol in symbol_string.split(','):
            market_cap, price = get_market_cap_and_price(symbol, api_key)
            final_dataframe = final_dataframe.append(
                pd.Series(
                    [symbol, price, market_cap],
                    index=csv_columns
                ),
                ignore_index=True
            )

    return final_dataframe

def calculate_number_of_shares(final_dataframe: pd.DataFrame, portfolio_value: float) -> pd.DataFrame:
    """
    Calculates the number of shares to buy for each stock in a DataFrame based on a given portfolio value.
    
    Parameters:
    final_dataframe (pd.DataFrame): A DataFrame containing the stock data.
    portfolio_value (float): The total value of the portfolio.
    
    Returns:
    pd.DataFrame: A DataFrame containing the stock data along with the number of shares to buy and the order cost.
    """
    position_size = portfolio_value / len(final_dataframe.index)
    for i in range(len(final_dataframe)):
        final_dataframe.loc[i, 'Number of Shares to Buy'] = math.floor(position_size / final_dataframe.loc[i, 'Stock Price'])
        final_dataframe.loc[i, 'Order Cost'] = final_dataframe.loc[i, 'Number of Shares to Buy'] * final_dataframe.loc[i, 'Stock Price']

    return final_dataframe
  
def create_excel_file(final_dataframe: pd.DataFrame, excel_file_path: str) -> None:
    """
    Creates an Excel file containing the stock data.
    
    Parameters:
    final_dataframe (pd.DataFrame): A DataFrame containing the stock data.
    excel_file_path (str): The file path to the Excel file to create.
    
    Returns:
    None
    """
    writer = pd.ExcelWriter(excel_file_path, engine='xlsxwriter')
    final_dataframe.to_excel(writer, sheet_name='Recommended Trades', index=False)

    background_color = '#0a0a23'
    font_color = '#ffffff'

    string_format = writer.book.add_format(
        {
            'font_color': font_color,
            'bg_color': background_color,
            'border': 1
        }
    )

    dollar_format = writer.book.add_format(
        {
            'num_format': '$0.00',
            'font_color': font_color,
            'bg_color': background_color,
            'border': 1
        }
    )

    integer_format = writer.book.add_format(
        {
            'num_format': '0',
            'font_color': font_color,
            'bg_color': background_color,
            'border': 1
        }
    )

    column_formats = {
        'A': ['Ticker', string_format],
        'B': ['Stock Price', dollar_format],
        'C': ['Market Capitalization', dollar_format],
        'D': ['Number of Shares to Buy', integer_format],
        'E': ['Order Cost', dollar_format]
    }

    for column in column_formats.keys():
        writer.sheets['Recommended Trades'].set_column(f'{column}:{column}', 25, column_formats[column][1])
        writer.sheets['Recommended Trades'].write(f'{column}1', column_formats[column][0], column_formats[column][1])

    writer.save()

'''
This code performs fundamental analysis on a given stock ticker by calculating three financial ratios: P/E (price-to-earnings) ratio, P/B (price-to-book) ratio, and P/S (price-to-sales) ratio. It downloads financial statements from Yahoo Finance, calculates the financial ratios using historical stock data, and generates a report with the financial statements and ratios for the specified ticker. It also provides the option to perform the same analysis on a list of ticker symbols.
'''

import yfinance as yf
import pandas as pd


def calculate_pe_ratio(close_price, eps):
    """
    Calculates the Price-to-Earnings (P/E) Ratio.
    """
    return close_price / eps


def calculate_pb_ratio(close_price, book_value_per_share):
    """
    Calculates the Price-to-Book (P/B) Ratio.
    """
    return close_price / book_value_per_share


def calculate_ps_ratio(close_price, revenue_per_share):
    """
    Calculates the Price-to-Sales (P/S) Ratio.
    """
    return close_price / revenue_per_share


def get_financial_ratios(df):
    """
    Calculates the financial ratios needed for Fundamental Analysis.
    """
    close_price = df['Close'][-1]
    eps = df['Earnings/Share'][-1]
    book_value_per_share = df['Book Value'][-1]
    revenue_per_share = df['Revenue/Share'][-1]

    ratios = {
        'P/E Ratio': calculate_pe_ratio(close_price, eps),
        'P/B Ratio': calculate_pb_ratio(close_price, book_value_per_share),
        'P/S Ratio': calculate_ps_ratio(close_price, revenue_per_share)
    }

    return ratios


def get_financial_statements(ticker_symbol):
    """
    Retrieves the financial statements for a given ticker symbol from Yahoo Finance.
    """
    stock_data = yf.Ticker(ticker_symbol)
    income_statement = stock_data.financials.loc[['Total Revenue', 'Gross Profit', 'Operating Income']]
    balance_sheet = stock_data.balance_sheet.loc[['Total Assets', 'Total Liabilities', 'Total Stockholder Equity']]
    cash_flow = stock_data.cashflow.loc[['Total Cash From Operating Activities', 'Total Cashflows From Investing Activities', 'Total Cashflows From Financing Activities']]
    
    return income_statement, balance_sheet, cash_flow


def analyze_fundamentals(ticker_symbol):
    """
    Performs Fundamental Analysis on a single stock.
    """
    income_statement, balance_sheet, cash_flow = get_financial_statements(ticker_symbol)
    history = yf.Ticker(ticker_symbol).history(period='max')
    financial_ratios = get_financial_ratios(history)

    report = {
        'ticker': ticker_symbol,
        'income_statement': income_statement.to_dict(),
        'balance_sheet': balance_sheet.to_dict(),
        'cash_flow': cash_flow.to_dict(),
        'financial_ratios': financial_ratios
    }

    return report


def analyze_fundamentals_batch(ticker_symbols):
    """
    Performs Fundamental Analysis on a list of stocks.
    """
    reports = [analyze_fundamentals(ticker_symbol) for ticker_symbol in ticker_symbols]
    return reports

import yfinance as yf
import pandas as pd

def calculate_ratios(df):
    """
    Calculates the ratios needed for Fundamental Analysis.
    """
    ratios = {}

    # Calculate P/E Ratio
    ratios['P/E Ratio'] = df['Close'][-1] / df['Earnings/Share'][-1]

    # Calculate P/B Ratio
    ratios['P/B Ratio'] = df['Close'][-1] / df['Book Value'][-1]

    # Calculate P/S Ratio
    ratios['P/S Ratio'] = df['Close'][-1] / df['Revenue/Share'][-1]

    return ratios

def analyze_fundamentals(ticker_symbol):
    """
    Performs Fundamental Analysis on a single stock.
    """
    # Download data from Yahoo Finance
    stock_data = yf.Ticker(ticker_symbol)

    # Get financial statements
    income_statement = stock_data.financials.loc[['Total Revenue', 'Gross Profit', 'Operating Income']]
    balance_sheet = stock_data.balance_sheet.loc[['Total Assets', 'Total Liabilities', 'Total Stockholder Equity']]
    cash_flow = stock_data.cashflow.loc[['Total Cash From Operating Activities', 'Total Cashflows From Investing Activities', 'Total Cashflows From Financing Activities']]

    # Calculate financial ratios
    financial_ratios = calculate_ratios(stock_data.history(period="max"))

    # Create report
    report = f"\nFundamental Analysis Report for {ticker_symbol}\n\n"

    report += "Income Statement:\n"
    report += f"{income_statement}\n\n"

    report += "Balance Sheet:\n"
    report += f"{balance_sheet}\n\n"

    report += "Cash Flow:\n"
    report += f"{cash_flow}\n\n"

    report += "Financial Ratios:\n"
    for ratio, value in financial_ratios.items():
        report += f"{ratio}: {value:.2f}\n"

    return report

def analyze_fundamentals_batch(ticker_symbols):
    """
    Performs Fundamental Analysis on a list of stocks.
    """
    reports = []
    for ticker_symbol in ticker_symbols:
        report = analyze_fundamentals(ticker_symbol)
        reports.append(report)

    return reports

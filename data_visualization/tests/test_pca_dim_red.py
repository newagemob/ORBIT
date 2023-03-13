import unittest
import pandas as pd
from pca_dim_red import perform_pca
from data_collection.scrape_stock_data import scrape_sp500_stocks


def main():
    df = scrape_sp500_stocks()
    df = perform_pca(df, 2)
    print(df)

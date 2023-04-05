"""
  This pipeline
  
  1. Scrape the current S&P 500 companies from data_collection.scrape_stock_data.scrape_sp500_stocks() and puts them into a CSV file in data_collection/output/sp500_stocks.csv
  
  2. Visualize the data for both human-readable and machine-readable purposes.
  The human-readable visualization shows the top 10 companies of any given CSV data_collection/output/_.csv file, then returns top 10 and bottom 10 companies for the year and week.
  The machine-readable visualization is a CSV file of the top 10 companies by market cap in data_visualization/output/sp500_stocks.csv
  
"""


# 1. Data Collection (Scraping current and historical data)
# import methods.data_collection.run as scraper
# run the data collection script
# scraper

# 2. Human + Machine Readable Data Visualization
import methods.data_analysis.data_visualization.run as analyzer
# run the data analysis script
analyzer

# 3. Create / Update the Machine Learning Model


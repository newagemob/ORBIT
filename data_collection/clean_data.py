'''
This script uses a function to encapsulate the cleaning and preprocessing steps, which makes it easy to reuse the code for different datasets. The function takes four arguments: the input file path, the output file path, the start date for the time period to filter the data, and the end date for the time period to filter the data. The function returns the cleaned and preprocessed data as a Pandas DataFrame.
'''

import pandas as pd

def read_csv(input_file):
    """
    Reads a CSV file into a Pandas DataFrame.
    """
    return pd.read_csv(input_file)

def drop_missing_values(df):
    """
    Drops rows with missing values in a Pandas DataFrame.
    """
    return df.dropna()

def convert_to_datetime(df, date_col):
    """
    Converts a date column in a Pandas DataFrame to datetime format.
    """
    df[date_col] = pd.to_datetime(df[date_col])
    return df

def filter_by_date(df, start_date, end_date, date_col):
    """
    Filters a Pandas DataFrame to a specific time period based on a date column.
    """
    return df.loc[(df[date_col] >= start_date) & (df[date_col] <= end_date)]

def drop_columns(df, columns):
    """
    Drops specific columns from a Pandas DataFrame.
    """
    return df.drop(columns=columns, axis=1)

def group_by_date(df, date_col, value_col):
    """
    Groups a Pandas DataFrame by a date column and calculates the average value of a specified column.
    """
    return df.groupby(date_col)[value_col].mean().reset_index()

def rename_columns(df, col_dict):
    """
    Renames columns in a Pandas DataFrame based on a dictionary.
    """
    return df.rename(columns=col_dict)

def save_to_csv(df, output_file):
    """
    Saves a Pandas DataFrame to a CSV file.
    """
    df.to_csv(output_file, index=False)

def clean_and_preprocess_data(input_file, output_file, start_date, end_date):
    """
    Cleans and preprocesses a stock data CSV file.
    """
    # Read CSV file
    df = read_csv(input_file)
    
    # Drop missing values
    df = drop_missing_values(df)
    
    # Convert date column to datetime format
    df = convert_to_datetime(df, 'date')
    
    # Filter data for specific time period
    df = filter_by_date(df, start_date, end_date, 'date')
    
    # Drop columns not needed for analysis
    df = drop_columns(df, ['column1', 'column2'])
    
    # Group data by date and calculate average price
    df = group_by_date(df, 'date', 'price')
    
    # Rename columns for consistency
    df = rename_columns(df, {'date': 'Date', 'price': 'Price'})
    
    # Save cleaned and preprocessed data to a new csv file
    save_to_csv(df, output_file)
    
    return df

# Define input and output file paths
input_file = 'raw_stock_data.csv'
output_file = 'cleaned_stock_data.csv'

# Define start and end dates for time period to filter data
start_date = pd.to_datetime('2022-01-01')
end_date = pd.to_datetime('2022-12-31')

# Clean and preprocess data
clean_and_preprocess_data(input_file, output_file, start_date, end_date)

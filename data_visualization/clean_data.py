'''
This script uses a function to encapsulate the cleaning and preprocessing steps, which makes it easy to reuse the code for different datasets. The function takes four arguments: the input file path, the output file path, the start date for the time period to filter the data, and the end date for the time period to filter the data. The function returns the cleaned and preprocessed data as a Pandas DataFrame.
'''

import pandas as pd

# Define function to clean and preprocess data
def clean_and_preprocess_data(input_file, output_file, start_date, end_date):
    
    # Import data
    df = pd.read_csv(input_file)
    
    # Drop rows with missing values
    df = df.dropna()
    
    # Convert date column to datetime format
    df['date'] = pd.to_datetime(df['date'])
    
    # Filter data for specific time period
    df = df.loc[(df['date'] >= start_date) & (df['date'] <= end_date)]
    
    # Drop columns not needed for analysis
    df = df.drop(['column1', 'column2'], axis=1)
    
    # Group data by date and calculate average price
    df = df.groupby('date').mean().reset_index()
    
    # Rename columns for consistency
    df = df.rename(columns={'date': 'Date', 'price': 'Price'})
    
    # Save cleaned and preprocessed data to a new csv file
    df.to_csv(output_file, index=False)
    
    return df

# Define input and output file paths
input_file = 'raw_stock_data.csv'
output_file = 'cleaned_stock_data.csv'

# Define start and end dates for time period to filter data
start_date = pd.to_datetime('2022-01-01')
end_date = pd.to_datetime('2022-12-31')

# Clean and preprocess data
clean_and_preprocess_data(input_file, output_file, start_date, end_date)

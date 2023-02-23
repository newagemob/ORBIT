import pandas as pd
from hypothesis import hypothesis_testing

# Import data
data = pd.read_csv('cleaned_stock_data.csv')

# Conduct hypothesis test
t_stat, p_val = hypothesis_testing(data, 'feature', 'group1', 'group2')

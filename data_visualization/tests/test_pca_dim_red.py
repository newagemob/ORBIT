import pandas as pd
from pca_dim_red import perform_pca

# Load the input data
df = pd.read_csv('my_data.csv')

# Perform PCA and keep 2 components
transformed_df = perform_pca(df, 2)

# Save the transformed data to a CSV file
transformed_df.to_csv('transformed_data.csv', index=False)

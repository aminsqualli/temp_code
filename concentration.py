import pandas as pd

# Sample dataframe
data = {
    'name': ['A', 'A', 'B', 'B', 'C', 'C'],
    'concentration': [0.1, 0.3, 0.2, 0.4, 0.5, 0.1],
    'ticker': ['X', 'Y', 'Z', 'W', 'T', 'U']
}
df = pd.DataFrame(data)

# Find the ticker with the highest concentration for each name
max_concentration_df = df.loc[df.groupby('name')['concentration'].idxmax()]

# Set the name as the index
max_concentration_df.set_index('name', inplace=True)

# Keep only the ticker column
result_df = max_concentration_df[['ticker']]

result_df
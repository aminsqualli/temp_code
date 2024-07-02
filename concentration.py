import pandas as pd

# Sample dataframe
data = {
    'name': ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'C', 'C'],
    'concentration': [0.1, 0.3, 0.2, 0.4, 0.5, 0.6, 0.2, 0.4, 0.3, 0.1, 0.5, 0.6, 0.5, 0.1, 0.3, 0.2, 0.6, 0.4],
    'ticker': ['X', 'Y', 'Z', 'W', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
}
df = pd.DataFrame(data)

# Get the top five tickers with the highest concentration for each name
top5_concentration_df = df.sort_values(by=['name', 'concentration'], ascending=[True, False])
top5_concentration_df = top5_concentration_df.groupby('name').head(5)

# Create a new dataframe indexed by name and showing the top five tickers
result_df = top5_concentration_df.set_index('name').sort_index()

# If you want to see only the tickers, you can filter the dataframe
result_df = result_df[['ticker', 'concentration']]

import ace_tools as tools; tools.display_dataframe_to_user(name="Top 5 Tickers by Concentration", dataframe=result_df)
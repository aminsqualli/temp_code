import pandas as pd

# Sample DataFrame
data = {'isin': ['ABC', 'DEF', 'ABC', 'DEF', 'XYZ'],
        'values': [10, 20, 30, 40, 50],
        'other_column': ['A', 'B', 'C', 'D', 'E']}
df = pd.DataFrame(data)

# Group by 'isin' and sum 'values'
result_df = df.groupby('isin', as_index=False).agg({'values': 'sum', 'other_column': 'first'})

print(result_df)
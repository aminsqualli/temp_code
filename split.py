import pandas as pd
import math

def split_dataframe(df):
    new_rows = []

    def split_values(index, value, other_columns):
        max_value_per_row = 50
        num_rows = math.ceil(value / max_value_per_row)

        for i in range(num_rows):
            new_index = f"{index}_{i + 1}"
            new_value = min(max_value_per_row, value - i * max_value_per_row)
            new_rows.append({'index': new_index, 'values': new_value, **other_columns})

    for _, row in df.iterrows():
        split_values(row['index'], row['values'], row.drop(['index', 'values']))

    return pd.DataFrame(new_rows)

# Sample DataFrame with additional columns
data = {'index': ['A', 'B', 'C'],
        'values': [105, 30, 80],
        'other_column': ['X', 'Y', 'Z']}
df = pd.DataFrame(data)

# Split the DataFrame
df_split = split_dataframe(df)

# Display the result
print(df_split)
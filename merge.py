import pandas as pd

# Sample DataFrame after splitting
data_split = {'index': ['A_1', 'A_2', 'A_3', 'B', 'C_1', 'C_2'],
              'values': [50, 50, 5, 30, 50, 30]}
df_split = pd.DataFrame(data_split)

# Function to merge split rows
def merge_rows(df_split):
    merged_rows = []

    for _, row in df_split.iterrows():
        parts = row['index'].split('_')
        original_index = parts[0]

        if len(parts) == 2:
            index_number = int(parts[1])
            if index_number == 1:
                merged_rows.append({'index': original_index, 'values': row['values']})
            else:
                merged_rows[-1]['values'] += row['values']

        else:
            merged_rows.append({'index': original_index, 'values': row['values']})

    return pd.DataFrame(merged_rows)

# Create a new DataFrame with merged rows
result_merged_df = merge_rows(df_split)

# Display the result
print(result_merged_df)
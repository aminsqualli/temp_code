import pandas as pd

def merge_dataframe(df_split):
    merged_rows = []

    for _, row in df_split.iterrows():
        parts = row['index'].split('_')
        original_index = parts[0]

        if len(parts) > 1:
            index_number = int(parts[1])
            if index_number == 1:
                merged_rows.append({'index': original_index, 'values': row['values'], **row.drop(['index', 'values']).to_dict()})
            else:
                merged_rows[-1]['values'] += row['values']

        else:
            merged_rows.append({'index': original_index, 'values': row['values'], **row.drop(['index', 'values']).to_dict()})

    return pd.DataFrame(merged_rows)

# Sample DataFrame after splitting
data_split = {'index': ['A_1', 'A_2', 'A_3', 'B', 'C_1', 'C_2'],
              'values': [50, 50, 5, 30, 50, 30],
              'other_column': ['X', 'X', 'X', 'Y', 'Z', 'Z']}
df_split = pd.DataFrame(data_split)

# Merge the DataFrame back
df_merged = merge_dataframe(df_split)

# Display the result
print(df_merged)
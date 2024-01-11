import pandas as pd
import math

# Sample DataFrame
data = {'index': ['A', 'B', 'C'],
        'values': [105, 30, 80]}
df = pd.DataFrame(data)

# New DataFrame to store the split rows
new_rows = []

# Function to split values into rows
def split_values(index, value):
    max_value_per_row = 50
    num_rows = math.ceil(value / max_value_per_row)

    for i in range(num_rows):
        new_index = f"{index}_{i + 1}"
        new_value = min(max_value_per_row, value - i * max_value_per_row)
        new_rows.append({'index': new_index, 'values': new_value})

# Iterate through the original DataFrame
for _, row in df.iterrows():
    split_values(row['index'], row['values'])

# Create a new DataFrame with split rows
result_df = pd.DataFrame(new_rows)

# Display the result
print(result_df)
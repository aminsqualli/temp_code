import pandas as pd

# Create sample data matching your example
data = {
    'col1': [['hello', 'world']],
    'col2': [['bye', 'world']],
    'col3': ['some info'],
    'col4': [42],
    'col5': ['more data'],
    'col6': [True],
    'col7': [3.14],
    'col8': ['extra'],
    'col9': [100],
    'col10': ['last column']
}

df = pd.DataFrame(data)

# Explode both columns while keeping other information
df_exploded = df.explode(['col1', 'col2'])

print("Original DataFrame:")
print(df)
print("\nExploded DataFrame:")
print(df_exploded)

# If you want to reset the index:
df_exploded = df_exploded.reset_index(drop=True)
print("\nExploded DataFrame with reset index:")
print(df_exploded)
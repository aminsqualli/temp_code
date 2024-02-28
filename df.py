import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows

# Load the existing workbook
workbook = load_workbook('existing_file.xlsx')

# Select the worksheet where you want to insert the DataFrame
worksheet = workbook['Sheet1']  # Change 'Sheet1' to your sheet name

# Create or load your DataFrame
data = {'Column1': [1, 2, 3],
        'Column2': ['A', 'B', 'C']}
df = pd.DataFrame(data)

# Get the rows from the DataFrame
rows = dataframe_to_rows(df, index=False, header=True)

# Determine the starting cell for the DataFrame
start_row = 1  # You can adjust this based on where you want to insert the DataFrame
start_column = 1

# Write the DataFrame to the worksheet
for r_idx, row in enumerate(rows, start=start_row):
    for c_idx, value in enumerate(row, start=start_column):
        worksheet.cell(row=r_idx, column=c_idx, value=value)

# Save the changes
workbook.save('existing_file.xlsx')
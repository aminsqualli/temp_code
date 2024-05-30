import pandas as pd
from openpyxl import Workbook

# Example dictionary with keys longer than 31 characters
data_dict = {
    'some_really_long_key_that_is_longer_than_31_characters_1': pd.DataFrame({'A': [1, 2, 3]}),
    'another_really_long_key_that_is_longer_than_31_characters_2': pd.DataFrame({'B': [4, 5, 6]}),
    'some_really_long_key_that_is_longer_than_31_characters_2': pd.DataFrame({'C': [7, 8, 9]}),
}

# Create a new Excel workbook
wb = Workbook()
ws = wb.active
ws.title = "Sheet1"

# Initialize a counter
counter = {}

# Loop through the dictionary and save each dataframe to a sheet
with pd.ExcelWriter('output.xlsx', engine='openpyxl') as writer:
    for key, df in data_dict.items():
        # Slice the key to 31 characters
        short_key = key[:31]
        
        # If the short key is already used, append a counter to ensure uniqueness
        if short_key in counter:
            counter[short_key] += 1
            sheet_name = f"{short_key}_{counter[short_key]}"
        else:
            counter[short_key] = 0
            sheet_name = short_key
        
        # Write the dataframe to the Excel sheet
        df.to_excel(writer, sheet_name=sheet_name, index=False)

# Save the workbook
wb.save('output.xlsx')
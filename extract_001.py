import pandas as pd
import re

# Sample list of strings
data_list = ['cusip="67372" isin="63727282" symbol="AAPL"',
             'cusip="12345" isin="98765432" symbol="GOOG"',
             'isin="98765433" symbol="MSFT"',
             'cusip="54321"']

# Initialize lists to store extracted values
cusips = []
isins = []
symbols = []

# Define regular expression pattern to extract values
pattern = r'(?:(?:cusip="([^"]*)")?\s*)?(?:(?:isin="([^"]*)")?\s*)?(?:(?:symbol="([^"]*)")?)?'

# Parse each string in the list and extract values using regular expressions
for item in data_list:
    match = re.match(pattern, item)
    if match:
        cusips.append(match.group(1) if match.group(1) else 'N/A')  # Set default value if 'cusip' is missing
        isins.append(match.group(2) if match.group(2) else 'N/A')    # Set default value if 'isin' is missing
        symbols.append(match.group(3) if match.group(3) else 'N/A')  # Set default value if 'symbol' is missing
    else:
        print(f"Failed to parse string: {item}")

# Create DataFrame from the extracted values
df = pd.DataFrame({'cusip': cusips, 'isin': isins, 'symbol': symbols})

# Display the DataFrame
print(df)
import pandas as pd

# Sample list of strings
data_list = ['cusip="67372" isin="63727282" symbol="AAPL"',
             'cusip="12345" isin="98765432" symbol="GOOG"']

# Initialize lists to store extracted values
cusips = []
isins = []
symbols = []

# Parse each string in the list and extract values
for item in data_list:
    parts = item.split()  # Split the string into parts
    cusip = parts[0].split('=')[1].strip('"')  # Extract cusip value
    isin = parts[1].split('=')[1].strip('"')   # Extract isin value
    symbol = parts[2].split('=')[1].strip('"') # Extract symbol value
    cusips.append(cusip)
    isins.append(isin)
    symbols.append(symbol)

# Create DataFrame from the extracted values
df = pd.DataFrame({'cusip': cusips, 'isin': isins, 'symbol': symbols})

# Display the DataFrame
print(df)
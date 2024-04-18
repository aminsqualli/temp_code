import pandas as pd
import re

# Sample list of strings
data_list = ['cusip="67372" isin="63727282" sedol="1234567" symbol="AAPL" secname="Apple Inc." country="US" sectype="Equity"',
             'cusip="12345" isin="98765432" symbol="GOOG" secname="Alphabet Inc." country="US" sectype="Equity"',
             'isin="98765433" symbol="MSFT" secname="Microsoft Corporation" country="US" sectype="Equity"',
             'cusip="54321"']

# Initialize lists to store extracted values
cusips = []
isins = []
sedols = []
symbols = []
secnames = []
countries = []
sectypes = []

# Define regular expression pattern to extract values
pattern = r'(?:cusip="([^"]*)"|isin="([^"]*)"|sedol="([^"]*)"|symbol="([^"]*)"|secname="([^"]*)"|country="([^"]*)"|sectype="([^"]*)")?'

# Parse each string in the list and extract values using regular expressions
for item in data_list:
    match = re.findall(pattern, item)
    if match:
        cusips.append(match[0][0] if match[0][0] else 'N/A')
        isins.append(match[0][1] if match[0][1] else 'N/A')
        sedols.append(match[0][2] if match[0][2] else 'N/A')
        symbols.append(match[0][3] if match[0][3] else 'N/A')
        secnames.append(match[0][4] if match[0][4] else 'N/A')
        countries.append(match[0][5] if match[0][5] else 'N/A')
        sectypes.append(match[0][6] if match[0][6] else 'N/A')
    else:
        print(f"Failed to parse string: {item}")

# Create DataFrame from the extracted values
df = pd.DataFrame({'cusip': cusips, 'isin': isins, 'sedol': sedols, 'symbol': symbols, 'secname': secnames, 'country': countries, 'sectype': sectypes})

# Display the DataFrame
print(df)
import win32com.client
import pandas as pd
from bs4 import BeautifulSoup

# Create an instance of the Outlook application
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

# Get the Inbox folder
inbox = outlook.GetDefaultFolder(6)  # 6 corresponds to the Inbox folder

# Iterate through the items in the Inbox folder (emails)
for item in inbox.Items:
    # Extract the HTML body of the email
    html_body = item.HTMLBody
    
    # Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(html_body, 'html.parser')
    
    # Find the table element
    table = soup.find('table')
    
    # If table is found
    if table:
        # Extract row data
        row_data = []
        for row in table.find_all('tr'):
            row_data.append([cell.text.strip() for cell in row.find_all('td')])
        
        # Create column titles
        num_columns = len(row_data[0])
        columns = [f'Column {i+1}' for i in range(num_columns)]
        
        # Create DataFrame
        df = pd.DataFrame(row_data, columns=columns)
        print("DataFrame from email:")
        print(df)
    else:
        print("No table found in email.")
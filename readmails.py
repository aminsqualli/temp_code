import win32com.client

# Connect to Outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)  # "6" refers to the Inbox folder

# Process emails in batches
batch_size = 100
start_index = 0
while True:
    # Get emails in the current batch
    batch_emails = inbox.Items[start_index:start_index + batch_size]

    # Process current batch
    for email in batch_emails:
        # Process each email as needed
        pass

    # Check if there are more emails to process
    if len(batch_emails) < batch_size:
        break

    start_index += batch_size
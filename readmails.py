import win32com.client

# Connect to Outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)  # "6" refers to the Inbox folder

# Process emails in batches
batch_size = 100
start_index = 0
total_emails = inbox.Items.Count

while start_index < total_emails:
    # Get emails in the current batch
    batch = inbox.Items.Sort("[ReceivedTime]", True)
    batch = batch[start_index:start_index + batch_size]

    # Check if the batch is not None
    if batch is not None:
        # Process each email in the batch
        for email in batch:
            # Process each email as needed
            print("Subject:", email.Subject)
            print("Sender:", email.SenderName)
            print("Received Time:", email.ReceivedTime)
            print("-------------------")

    # Update start index for the next batch
    start_index += batch_size
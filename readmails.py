import win32com.client

# Connect to Outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)  # "6" refers to the Inbox folder

# Process emails in batches
batch_size = 100
start_index = 0
while True:
    # Get emails in the current batch
    batch = inbox.Items
    batch.Sort("[ReceivedTime]", True)  # Sort by ReceivedTime in descending order
    batch = batch.Restrict("[ReceivedTime] >= '01/01/2024'")  # Adjust the date as needed
    batch = batch.GetFirst()
    for _ in range(start_index, start_index + batch_size):
        if not batch:
            break
        # Process each email as needed
        print("Subject:", batch.Subject)
        print("Sender:", batch.SenderName)
        print("Received Time:", batch.ReceivedTime)
        print("-------------------")
        batch = batch.GetNext()

    # Check if there are more emails to process
    if not batch:
        break

    start_index += batch_size
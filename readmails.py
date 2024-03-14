import win32com.client
import datetime

# Connect to Outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)  # "6" refers to the Inbox folder

# Get today's date
today = datetime.datetime.today()

# Define batch size
batch_size = 100

# Process emails received today in batches
emails_processed = 0
while True:
    # Get emails in the current batch
    batch_emails = []
    for email in inbox.Items:
        if email.Class == 43 and email.ReceivedTime.date() == today.date():
            batch_emails.append(email)
            emails_processed += 1
            if emails_processed == batch_size:
                break
    
    # Process current batch
    for email in batch_emails:
        print("Subject:", email.Subject)
        print("Sender:", email.SenderName)
        print("Received Time:", email.ReceivedTime)
        print("-------------------")
    
    # Check if we need to break the loop
    if emails_processed < batch_size:
        break
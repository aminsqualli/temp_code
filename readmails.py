import win32com.client
import datetime

def process_emails(emails):
    for email in emails:
        print("Subject:", email.Subject)
        print("Sender:", email.SenderName)
        print("Received Time:", email.ReceivedTime)
        print("-------------------")

# Connect to Outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)  # "6" refers to the Inbox folder

# Get today's date
today = datetime.datetime.today()

# Define batch size
batch_size = 100

# Process emails in batches
start_index = 0
while True:
    end_index = start_index + batch_size
    batch = inbox.Items.Restrict("[ReceivedTime] >= '" + today.strftime('%m/%d/%Y') + "'")[start_index:end_index]
    if len(batch) == 0:
        break
    process_emails(batch)
    start_index = end_index
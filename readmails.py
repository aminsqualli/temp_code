import win32com.client
import datetime

# Connect to Outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)  # "6" refers to the Inbox folder

# Get today's date
today = datetime.datetime.today()

# Process emails received today
for email in inbox.Items:
    if email.Class == 43:  # Class 43 refers to a mail item
        if email.ReceivedTime.date() == today.date():
            print("Subject:", email.Subject)
            print("Sender:", email.SenderName)
            print("Received Time:", email.ReceivedTime)
            print("-------------------")
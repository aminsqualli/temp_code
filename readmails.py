import win32com.client
import datetime

# Connect to Outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)  # "6" refers to the Inbox folder

# Get today's date
today = datetime.datetime.today()

# Get emails received today
received_today = inbox.Items.Restrict("[ReceivedTime] >= '" + today.strftime('%m/%d/%Y') + "'")

# Print subject and sender of each email received today
for email in received_today:
    print("Subject:", email.Subject)
    print("Sender:", email.SenderName)
    print("Received Time:", email.ReceivedTime)
    print("-------------------")
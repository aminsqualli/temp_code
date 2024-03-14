import win32com.client
import datetime

# Connect to Outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)  # "6" refers to the Inbox folder

# Get today's date
today = datetime.datetime.today()

# Get all emails from the inbox
all_emails = inbox.Items

# Filter emails received today
received_today = [email for email in all_emails if email.Class == 43 and email.ReceivedTime.date() == today.date()]

# Print subject and sender of each email received today
for email in received_today:
    print("Subject:", email.Subject)
    print("Sender:", email.SenderName)
    print("Received Time:", email.ReceivedTime)
    print("-------------------")
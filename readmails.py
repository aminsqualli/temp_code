import win32com.client
import datetime
import pytz

# Connect to Outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)  # "6" refers to the Inbox folder

# Get today's date
today = datetime.datetime.today()

# Set the time zone to the local time zone
local_timezone = pytz.timezone('YOUR_TIMEZONE')  # Replace 'YOUR_TIMEZONE' with your local time zone
today_local = datetime.datetime.now(local_timezone)

# Get the start of the day in the local time zone
start_of_day_local = today_local.replace(hour=0, minute=0, second=0, microsecond=0)

# Format the date string with the adjusted start of the day
date_string = start_of_day_local.strftime('%m/%d/%Y %H:%M:%S')

# Get emails received today
received_today = inbox.Items.Restrict("[ReceivedTime] >= '" + date_string + "'")

# Print subject and sender of each email received today
for email in received_today:
    print("Subject:", email.Subject)
    print("Sender:", email.SenderName)
    print("Received Time:", email.ReceivedTime)
    print("-------------------")
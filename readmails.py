import win32com.client
import datetime
import pytz

# Connect to Outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)  # "6" refers to the Inbox folder

# Define New York time zone
ny_timezone = pytz.timezone('America/New_York')

# Get today's date in New York time zone
today_ny = datetime.datetime.now(ny_timezone)

# Get the start of the day in New York time zone
start_of_day_ny = today_ny.replace(hour=0, minute=0, second=0, microsecond=0)

# Convert New York start of the day to UTC
start_of_day_utc = start_of_day_ny.astimezone(pytz.utc)

# Format the date string with the adjusted start of the day in UTC
date_string = start_of_day_utc.strftime('%m/%d/%Y %H:%M:%S')

# Get emails received today
received_today = inbox.Items.Restrict("[ReceivedTime] >= '" + date_string + "'")

# Print subject and sender of each email received today
for email in received_today:
    print("Subject:", email.Subject)
    print("Sender:", email.SenderName)
    print("Received Time:", email.ReceivedTime)
    print("-------------------")
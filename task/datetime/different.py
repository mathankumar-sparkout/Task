
from datetime import datetime
from pytz import timezone

format = "%Y-%m-%d %H:%M:%S %Z%z" #->(year,month,date hour,min,sec.utc)

# getting  current time in UTC timezone
now_utc = datetime.now(timezone('UTC'))

# Format the DateTime
print('Current Time in UTC TimeZone:',now_utc.strftime(format))

# Converting to Asia/Kolkata time zone
now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))

# Format  datetime using the strftime()
print('Current Time in Asia/Kolkata TimeZone:',now_asia.strftime(format))
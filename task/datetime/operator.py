from datetime import datetime, timedelta

# Adding 3 days to a date
start = datetime(2024, 1, 1)
end_date = start + timedelta(days=3)
print("New Date:", end_date)

# Calculating time difference
date1 = datetime(2024, 1, 1)
date2 = datetime(2024, 1, 10)
difference = date2 - date1
print("Difference:", difference.days, "days")


#--------------------------------------------------

var=datetime.now() # today date
var1=datetime(2024,5,2,5,30,30) #user date
cul=var-var1
print(cul) 



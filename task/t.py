
from datetime import datetime
import pytz              #->python time zone

#get the current datetime

unaware_object=datetime.now()
print('timezone naive:',unaware_object)

#standard UTC timezone

aware_object=datetime.now(pytz.utc)
print('timezone aware:',aware_object)

#Us/central timezone

aware_us_central=datetime.now(pytz.timezone('US/central'))
print("US timezone",aware_us_central)



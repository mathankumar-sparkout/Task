
import datetime

#current date----------

var=datetime.date.today()
print(var)

#current date & time---------
var=datetime.datetime.now()
print(var)

#user define the date&time-------
var=datetime.datetime(2024,6,7,7,40,00) #->(year,month,date,hours,min,sec)
print(var)


#------------------------------------------------------------------------------------------------------------------------------
#Formatting & parsing

#strftime

#(year)-----
var=datetime.datetime.now()
res=var.strftime("%y")
print("short version of year",res)
res1=var.strftime("%Y")
print("full version of year",res1)

#(month)--------
var=datetime.datetime.now()
res=var.strftime("%b")
print("short version of month",res)
res1=var.strftime("%B")
print("full version of month",res1)

#(day)--------

var=datetime.datetime.now()
res=var.strftime("%a")
print("short version of day",res)
res1=var.strftime("%A")
print("full version of day",res1)


#(hour)#->H(24 hour)->I(12 hour)->p(Am/Pm)-----------
var=datetime.datetime.now()
res=var.strftime("%H")
print("short version of time",res)
res1=var.strftime("%I")
print("full version of time",res1)
res2=var.strftime("%p")
print("AM/PM",res2)

#(min)-->M----------------
var=datetime.datetime.now()
res=var.strftime("%M")
print("minutes",res)

#(sec)--S----------------

var=datetime.datetime.now()
res=var.strftime("%S")
print("seconds",res)

#micro(sec)-->f
var=datetime.datetime.now()
res=var.strftime("%f")
print("micro sec",res)

#---------------------------------------------------------------------------------------------------------------------









#check value

import re          #-> import package re
x="a"              #-> 
if re.match("a-z","a"): #-. match the value (.any number of character allow)->if true 
    print(True)
else:
    print(False)

#check correct space value--------

x="ma"
if re.match("..","ma"): #->.. corectly work on 2 character (true)otherwise false
    print(True)
else:
    print(False)
#center value check----------
x="aos"
if re.match("a.s","aos"): #-> . is consider by o-> value true
    print(True)
else:
    print(False)

#.*...........
x="hii python"
if re.match(".*i.p.",x): #->.* identifiy stating with 0 so(.*-take first value)
    print(True)
else:
    print(False)

#->end value------------
x="python"
if re.match(".*p.t.on$",x):#-> last value use ($)
    print(True)
else:
    print(False)

#(.+)..............
x="sabc"
if re.match(".+a.c",x): #-> atleast 1 character in first
    print(True)
else:
    print(False)
#................
x="mathan@123.com"
if re.match("[a-z]+@[a-z0-9]+\.[a-z]",x):#-> find the correct email id 
    print(True)
else:
    print(False)



#input expression

n=input()
if re.match("[0-91-9]$",n):#-> only work on 1-9 input values
    print(True)
else:
    print(False)
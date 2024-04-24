import os,stat,sys

from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 

# accessing and printing value
print(os.getenv("MY_KEY"))

print(os.getenv("HOST"))

#accessing the password value
print(os.getenv("PASSWORD"))

#***current directories***----------
print(os.getcwd())

#***list of files in folder***
print(os.listdir()) 

#***list of os functions***
print(dir(os)) #->os list of functions

#***change directories***
os.chdir("D:\python git\OOPS")
print(os.getcwd())

#***create a file
os.mkdir("os.txt")
print(os.getcwd())



#**delete a file
os.rmdir("os.txt")
print(os.getcwd())




#***rename*****
#os.rename("op.txt","Op.txt")
#print(os.listdir())


#***Checking if a path exists and if it is a file or directory****
var = os.path.exists("D:\python git\OOPS") 
print(var) 



#***split the path****
var = os.path.split("D:\python git\OOPS")
print(var)



#***join the path******
var = os.path.join("D:\python git\OOPS")
print(var)





# Open a file ****
fd = os.open('D:\python git\OOPS\op.py', os.O_WRONLY | os.O_CREAT)#->flag & mode
# Write to the file 
os.write(fd, b"Hello, world!")
# Close the 
os.close(fd)



#chmod()

# set path , set a file execute by the group
os.chmod("D:\python git\OOPS\op.py'", stat.S_IXGRP)
# Set a file write by others
os.chmod("D:\python git\OOPS\op.py'", stat.S_IWOTH)
print ("Changed mode successfully")





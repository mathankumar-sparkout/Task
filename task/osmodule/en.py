import os,stat,sys

from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 

# accessing and printing value
print(os.getenv("MY_KEY"))
#accessing the Host value
print(os.getenv("HOST"))

#accessing the password value
print(os.getenv("PASSWORD"))


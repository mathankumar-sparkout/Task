from pydantic import BaseModel,Field



#USER BASEMODEL
class User(BaseModel):
    User_id:int
    User_name:str|None=None
    User_age:int 
    User_address:str|None=None
    
#ADMIN BASEMODEL
class Admin(BaseModel):
    Admin_id:int
    Admin_name:str
    Admin_address:str|None=None
    

#USER RESPONSE MODEL
class User_response(BaseModel):
    User_name:str
    User_age:int
    User_address:str
    
#ADMIN RESPONSE MODEL
class Admin_response(BaseModel):
    Admin_name:str
    Admin_address:str

#USER DICTIONARY
users_dictionary = {1: {"User_name": "kumar", "User_age": 25, "User_address":"chennai"}}

#ADMIN DICTIONARY
admin_dictionary={1: {"Admin_name": "lokesh","Admin_address":"Coimbatore"}}
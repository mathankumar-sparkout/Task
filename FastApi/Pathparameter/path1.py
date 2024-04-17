from fastapi import FastAPI
from enum import Enum   #specfic type choose
app=FastAPI()

class user(str, Enum): # class 
    vegetables="vegetables"
    fruits="fruits"
    dairy="dairy"
 


@app.get("/food/{food_name}")
async def fun(food_name :user):
    if food_name == user.vegetables:  #-> user type ==user class same 
        return {"you are choose vegatables":food_name} #-> return user class value
    #elif(food_name ==user).fruits:
       # return {"you are choose fruits":food_name}
    if food_name.value == user.fruits:               #-> same thing
        return {"your are choose fruits":food_name}
    else:
        return {"you are choose dairy":food_name}




#doubts:
# elif->.value
#13.data type


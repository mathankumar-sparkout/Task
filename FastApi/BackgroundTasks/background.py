
from fastapi import FastAPI,BackgroundTasks # import background task
 
app=FastAPI()

def fun(email:str,message=""): 
    with open("log.txt",mode="w") as email_file: # file open and write a file
        content=f"notification{email}:{message}" 
        email_file.write(content)
        
@app.post("/notification/{emil}") # path parameter
async def notifi(email :str,background:BackgroundTasks): # background query parameter
    background.add_task(fun,email,message="some notification") # add the function (message:return log.txt)
    return{"message":"Notification send in the background"} # return msg
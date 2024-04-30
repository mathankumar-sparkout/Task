from typing import Annotated
from fastapi import FastAPI,Form #import form in fastapi

app=FastAPI()

@app.post("/user")
async def fun(username:Annotated[str,Form()],password:Annotated[str,Form()]):#-> username,password query parameter use the annotated function
    return username # return only username
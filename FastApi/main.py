#return string 
#get


from fastapi import FastAPI #-> import fastApi

app = FastAPI()  #-> app is fastapi


@app.get("/")   #-> dec the get op
async def root():
    return {"message": "Hello World"}





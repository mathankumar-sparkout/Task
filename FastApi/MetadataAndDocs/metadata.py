from fastapi import FastAPI

app=FastAPI(title="Python",
            description="description",
            summary="hello word",
            version=3.0,
            contact={
                "name":"fastapi",
                "url":"https:www.fastapi.com",
                "email":"fastapi@123.com",
            })
@app.get("/item")
async def fun():
    return [{"name":"java"}]





    
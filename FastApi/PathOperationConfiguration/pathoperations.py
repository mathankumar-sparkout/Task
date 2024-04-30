#response code---------------------------
from fastapi import FastAPI, status #import status in fastapi
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):  #basemodel
    name: str
    description: str | None = None # optional
    price: float
    tax: float | None = None
    tags: set[str] = set() #set


@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED,tags=["Item"],summary="create a items") #status_code 201 successfully message in 201
async def fun(item: Item): # request|class(Item)
    return item #return item

@app.get("/root",tags=["User"])
async def fun():
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return{"name":"python"}
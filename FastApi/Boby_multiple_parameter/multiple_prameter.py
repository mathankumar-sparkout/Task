from fastapi import FastAPI
from pydantic import BaseModel  # -> imported basemodel
from typing import Annotated

from fastapi import Body, FastAPI

app = FastAPI()


class item(BaseModel):  # -> add the first basemodel
    id: int
    name: str
    status: str | None


class user(BaseModel):  # ->add the second basemodel
    user_id: int
    user_name: str
    user_status: str | None


@app.put("/root/{item_id}")  # -> path parameter add {item_id}
async def fun(item_id: int, item: item, user: user, importance: Annotated[int, Body()]):
    return {"item_id": item_id, "user": user, "item": item, "importance": importance}

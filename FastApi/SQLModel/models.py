from sqlmodel import SQLModel,Field
from typing import Optional
#from pydantic import BaseModel


class User(SQLModel, table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(None, primary_key=True)
    name: str = None
    email: str = None
    password: str
    
#class res_User(BaseModel):
   ## name: str = None
    #email: int
    #password: str
    

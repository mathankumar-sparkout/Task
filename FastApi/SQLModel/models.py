from sqlmodel import SQLModel,Field
from typing import Optional


class User(SQLModel, table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(None, primary_key=True)
    name: str 
    email: str 
    password: str
    

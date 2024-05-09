from database import Base
from sqlalchemy import Column,Integer,String


class Blog(Base):
    __tablename__ ='blogs'
    id=Column(Integer,primary_key=True)
    title=Column(String(255))
    body=Column(String(200))
    
class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    name=Column(String(200))
    email=Column(String(200))
    password=Column(String(200))
    



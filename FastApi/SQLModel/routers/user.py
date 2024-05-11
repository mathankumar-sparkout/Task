from fastapi import APIRouter, Depends, status, HTTPException, Response
import database, models
from typing import List
from sqlmodel import Session,select
#from database import SessionLocal
from models import User
#from main import session


router = APIRouter(tags=["User"])

get_db = database.get_db




@router.post("/post_user")
# only we want name and password use this reponse_model
def create_user(request: models.User, db: Session = Depends(get_db)):
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=request.password
    )
    db.add(new_user) 
    db.commit() 
    db.refresh(new_user)
    return new_user


@router.get("/get_user",response_model=List[models.User],status_code=status.HTTP_200_OK)
def get_user():
    statement=select(models.User)
    result=Session.exec(statement).all()
    return result
    #blogs = Session.exec(models.User).all()
    #return blogs





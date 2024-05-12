from fastapi import APIRouter, Depends, status, HTTPException, Response
import database, models
from typing import List,Union
from sqlmodel import Session,select
from models import User
from database import engine


router = APIRouter(tags=["User"])

get_db = database.get_db






#get all user data----

@router.get("/get_all_user",response_model=List[models.User],status_code=status.HTTP_200_OK)
def get_user(db: Session = Depends(get_db)):
        stmt=select(models.User)
        result=db.exec(stmt).all()
        return result
    
    
# get single user data------

@router.get("/get_user/{id}",response_model=Union[models.User,str])
def get_single_user(id :int,response:Response,db: Session = Depends(get_db)):
        user=db.get(models.User, id)
        if user is None:
            response.status_code=404
            return {f"none{id}"}
        #result=jsonable_encoder(models.User)
        return user
    

@router.post("/post_user",response_model=models.User,status_code=201)
# only we want name and password use this reponse_model
def create_user(request: models.User, db: Session = Depends(get_db)):
    db.add(request) 
    db.commit() 
    db.refresh(request)
    return request

@router.put("/update_user/{id}",response_model=Union[models.User,str])
def update_user(id:int,update_user:models.User,response:Response,db:Session=Depends(get_db)):
    user=db.get(models.User,id)
  
    
    if user is None:
        response.status_code=404
        return "User not found"
    #user_dict= {"name": update_user.name, "email": update_user.email, "password": update_user.password}
    user_dict=update_user.dict(exclude_unset=True)
    for key,val in user_dict.items():
        setattr(user,key,val)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.delete("/delete user/{id}")
def delete_user(id:int,response:Response,db:Session=Depends(get_db)):
    user=db.get(models.User,id)
    if user is None:
        response.status_code=404
        return {"not found"}
    db.delete(user)
    db.commit()
    return Response(status_code=200)
    
    
    



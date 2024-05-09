from fastapi import (
    FastAPI,
    Depends,
    status,
    Response,
    HTTPException,
)  # import all things in Fastapi
import schemas, models  # import file(schemas,models)
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
import hashing


app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# post all data -----


@app.post(
    "/blog",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.show_Blog,
    tags=["blogs"],
)
async def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# all data return---
@app.get("/get_blog", response_model=List[schemas.show_Blog], tags=["blogs"])
# collection of blogs we want so we use List
async def get(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


# single data return----


@app.get("/get_singledata/{id}", response_model=schemas.show_Blog, tags=["blogs"])
# response_model work if we want which title or body basemodel(pydantic)
# choose the model(schemas->show_blog)
def singledata(id, response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not available",
        )
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {f"Blog with the id{id}is not available"}
    return blogs


# update the data----


@app.put(
    "/blog/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    response_class=Response,
    tags=["blogs"],
)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    blog.update({"title": request.title, "body": request.body})
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )
    db.commit()


# delete data in database----


@app.delete("/delete_data/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["blogs"])
def delete_blogs(id: int, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return {f"not avalaiable{id}"}


# CREATE NEW USER------------


@app.post("/post_user", response_model=schemas.showUser, tags=["User"])
# only we want name and password use this reponse_model
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=hashing.hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# GET USER DATA----------------


@app.get("/get_user/{id}", response_model=schemas.get_User, tags=["User"])
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"value {id} not in database"
        )
    return user


# UPDATE USER DATA---------------


@app.put(
    "/update_data/{id}",
    tags=["User"],
    response_class=Response,
    status_code=status.HTTP_202_ACCEPTED,
)
def update_data(id: int, request: schemas.User, db: Session = Depends(get_db)):
    update_user = db.query(models.User).filter(models.User.id == id)
    update_user.update(
        {"name": request.name, "email": request.email, "password": request.password}
    )

    if not update_user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )
    db.commit()


# DELETE USER DATA-----------------


@app.delete("/items/{id}", tags=["User"], status_code=status.HTTP_202_ACCEPTED)
async def delete_item(id: int):
    db = SessionLocal()
    db_item = db.query(models.User).filter(models.User.id == id).first()
    db.delete(db_item)
    db.commit()
    return {f"message": "data deleted {id} successfully"}

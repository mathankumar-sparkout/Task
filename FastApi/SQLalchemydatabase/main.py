from fastapi import FastAPI, Depends,status,Response,HTTPException
import schemas, models
from database import engine, SessionLocal
from sqlalchemy.orm import Session



app = FastAPI()


models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/blog",status_code=status.HTTP_201_CREATED)
async def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
#all data return---
@app.get("/get_blog")
async def get(db: Session = Depends(get_db)):
    blogs=db.query(models.Blog).all()
    return blogs
#single data return----
@app.get("/get_singledata/{id}")
def singledata(id,response:Response,db: Session = Depends(get_db)):
    blogs=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available")
        #response.status_code=status.HTTP_404_NOT_FOUND
        #return {f"Blog with the id{id}is not available"}
    return blogs

#delete data in database----

@app.delete("/delete_data/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete(id:int,db:Session=Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    db.commit()
    return{f"not avalaiable{id}"}
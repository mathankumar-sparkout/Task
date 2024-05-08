from fastapi import FastAPI, Depends
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


@app.post("/blog")
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
def singledata(id,db: Session = Depends(get_db)):
    blogs=db.query(models.Blog).filter(models.Blog.id==id).first()
    return blogs
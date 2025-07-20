from fastapi import FastAPI
from sqlalchemy.orm import Session 
from . import models,database

app = FastAPI()

# craete DB tables
models.base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def get_root():
    return {"message": "FastAPI with postgreSQL"}

@app.post("/users/")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    user = models.User(name = name, email = email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/users/", response_model=List[schemas.UserOut])
def read_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()
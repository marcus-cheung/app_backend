import uvicorn

from typing import List

from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session


import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency, return the session and close.


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/user/create", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)
    # return Response(status_code=status.HTTP_200_OK)


@app.get("/user/info", response_model=List[schemas.User])
def get_users(device_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_
    return


# To run locally
# if __name__ == '__main__':
    # uvicorn.run(app, port=5432)

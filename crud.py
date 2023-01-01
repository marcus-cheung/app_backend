from sqlalchemy.orm import Session
from bcrypt import gensalt, hashpw
import models
import schemas

# Profile creation

# Login


def create_user(db: Session, user: schemas.UserCreate):
    bytes = user.password.encode('utf-8')
    salt = gensalt()
    hashed_password = hashpw(bytes, salt)
    db_user = models.User(id=1,
                          email=user.email, hashed_password=hashed_password, salt=salt)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


# Hashes password. Returns hash and salt.


# def get_30_profiles(db: Session, )

from typing import List, Union
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    likes: List['User'] = []
    salt: bytes

    class Config:
        orm_mode = True

from sqlalchemy import Column, Integer, String
from .database import base

class User(base):
    tablename = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

from pydantic import BaseModel

class UserOut(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

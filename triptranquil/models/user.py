from sqlalchemy import Column, Integer, String, ForeignKey
from .base_model import BaseModel

class User(BaseModel):
    __tablename__ = 'users'
    email = Column(String(128), unique=True, nullable=False)
    role = Column(String(50), default="user")

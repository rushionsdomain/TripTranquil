from sqlalchemy import Column, Integer, ForeignKey
from .base_model import BaseModel

class Product(BaseModel):
    __tablename__ = 'products'
    destination = Column(String(128), nullable=False)
    price = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

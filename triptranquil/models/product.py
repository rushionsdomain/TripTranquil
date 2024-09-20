from sqlalchemy import Column, Integer, String, ForeignKey
from .base_model import Base

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    price = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

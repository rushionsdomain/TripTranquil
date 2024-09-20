from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config
from triptranquil.models.base_model import Base

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)

def get_session():
    return Session()

def init_db():
    Base.metadata.create_all(engine)

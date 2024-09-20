# triptranquil/session/session.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from triptranquil.models.user import User
from triptranquil.models.base_model import Base  # Assuming you have a base model
from triptranquil.models.trip import Trip  # Assuming Trip is defined

DATABASE_URL = "sqlite:///triptranquil.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def get_session():
    """Create a new session."""
    return Session()

def create_default_users():
    """Create default users and admins in the database."""
    session = get_session()
    users = [
        {"username": "Venus", "email": "Venus36@gmail.com", "password": "Meaw01"},
        {"username": "Joanne", "email": "Joanne77@gmail.com", "password": "Meaw02"},
        {"username": "Annet", "email": "Annet42@gmail.com", "password": "Meaw03"},
        {"username": "Victoria", "email": "Vicoria09@gmail.com", "password": "Meaw04"},
        {"username": "Bridget", "email": "Bridget52@gmail.com", "password": "Meaw05"},
    ]
    
    for user in users:
        new_user = User(username=user["username"], email=user["email"])
        new_user.set_password(user["password"])
        session.add(new_user)

    admins = [
        {"username": "Rushion", "email": "Rushion18@gmail.com", "password": "Woof23", "is_admin": True},
        {"username": "Marvin", "email": "Marvin77@gmail.com", "password": "Woof24", "is_admin": True},
    ]
    
    for admin in admins:
        new_admin = User(username=admin["username"], email=admin["email"], is_admin=admin["is_admin"])
        new_admin.set_password(admin["password"])
        session.add(new_admin)

    session.commit()
    session.close()

def init_db():
    """Create the database tables and populate with default users."""
    Base.metadata.create_all(engine)
    create_default_users()

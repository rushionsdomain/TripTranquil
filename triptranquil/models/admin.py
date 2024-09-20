from sqlalchemy import Column, String
from .user import User

class Admin(User):
    __tablename__ = 'admins'
    admin_code = Column(String(50), nullable=False)

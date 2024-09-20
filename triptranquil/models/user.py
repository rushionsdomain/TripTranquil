# triptranquil/models/user.py

from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
from triptranquil.models.base_model import Base
from werkzeug.security import generate_password_hash, check_password_hash

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password_hash = Column(String)
    is_admin = Column(Boolean, default=False)

    bookings = relationship('Booking', back_populates='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# triptranquil/models/booking.py

from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from triptranquil.models.base_model import Base

class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    trip_id = Column(Integer, ForeignKey('trips.id'))
    booking_date = Column(DateTime)

    user = relationship('User', back_populates='bookings')
    trip = relationship('Trip')  # Assuming Trip model exists

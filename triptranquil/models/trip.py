from triptranquil.models.base_model import Base
from sqlalchemy import Column, Integer, String, Float, Date

class Trip(Base):
    __tablename__ = 'trips'
    
    id = Column(Integer, primary_key=True)
    destination = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    duration = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String)

    def __repr__(self):
        return f"<Trip {self.destination} from {self.start_date} to {self.end_date} (${self.price})>"

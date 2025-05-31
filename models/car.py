from sqlalchemy import Column, Integer, String, Float, Enum, DateTime
from sqlalchemy.orm import relationship
from config.db import Base
from datetime import datetime
import enum

class CarStatus(enum.Enum):
    available = "available"
    sold = "sold"

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    status = Column(Enum(CarStatus), default=CarStatus.available)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships to other models
    sales = relationship("Sale", back_populates="car")

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from config.db import Base
from datetime import datetime

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships to other models
    sales = relationship("Sale", back_populates="customer")

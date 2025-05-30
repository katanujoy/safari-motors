from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from config.db import Base
from datetime import datetime

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    position = Column(String, nullable=False) 
    email = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    sales = relationship("Sale", back_populates="employee")

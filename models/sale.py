from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from config.db import Base
from datetime import datetime

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    car_id = Column(Integer, ForeignKey("cars.id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    car = relationship("Car", back_populates="sales")
    customer = relationship("Customer", back_populates="sales")
    employee = relationship("Employee", back_populates="sales")

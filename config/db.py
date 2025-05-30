from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

# Base class for all models
Base = declarative_base()

# SQLite database engine
engine = create_engine("sqlite:///safari_motors.db", echo=True)

# Session factory for DB interaction
SessionLocal = sessionmaker(bind=engine)

# Helper function to get a new session
def get_session():
    return SessionLocal()

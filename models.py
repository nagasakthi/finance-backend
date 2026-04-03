from sqlalchemy import Column, Integer, String, Float, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    role = Column(String)  # viewer, analyst, admin
    is_active = Column(Boolean, default=True)

class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    type = Column(String)  # income / expense
    category = Column(String)
    date = Column(Date)
    notes = Column(String)
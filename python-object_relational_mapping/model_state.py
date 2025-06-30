#!/usr/bin/python3
"""
State class mapped to 'states' table
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# base class for all models
Base = declarative_base()

class State(Base):
    """State model"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)  # primary key
    name = Column(String(128), nullable=False)  # state name

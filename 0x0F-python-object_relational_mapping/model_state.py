#!/usr/bin/python3
"""
This module creates a table using sqlalchemy
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sys

#Session = sessionmaker(bind=engine)
#session = Session()

Base = declarative_base()

class State(Base):
    """State table"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

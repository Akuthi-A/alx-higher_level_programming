#!/usr/bin/python3

"""
python script that uses SQLAlchemy
python file that contains the class definition of a State and an instance Base = declarative_base()
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    State class - Table
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    name = Column(String(128), nullable=False)

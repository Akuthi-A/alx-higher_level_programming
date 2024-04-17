#!/usr/bin/python3
"""
This module creates a table using sqlalchemy
"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


class City(Base):
    """City table"""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('State.id'))

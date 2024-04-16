#!/usr/bin/python3
"""
lists all State objects from db hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys

engine = engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

Session = sessionmaker(bind=engine)
session = Session()

states = session.query(State).order_by(State.id)

for state in states:
    print(f"{state.id}: {state.name}")


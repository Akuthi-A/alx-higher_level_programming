#!/usr/bin/python3

"""
a script that prints the State object with the name passed as arg
from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(name=sys.argv[4]).first()
    
    if state:
        print(f"{state.id}")
        
    else:
        print("Not found")

    Base.metadata.create_all(engine)
    session.close()





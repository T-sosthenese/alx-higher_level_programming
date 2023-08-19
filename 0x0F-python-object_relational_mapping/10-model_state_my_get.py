#!/usr/bin/python3
"""
Printing the state id of the state provided as an argument.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1],
                           sys.argv[2],
                           sys.argv[3],
                           pool_pre_ping=True))
    Session = sessionmaker(bind=engine)
    session = Session()
    search_state = sys.argv[4]
    state = session.query(State).filter(State.name == search_state).first()
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()

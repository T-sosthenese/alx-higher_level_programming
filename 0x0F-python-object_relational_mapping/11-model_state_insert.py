#!/usr/bin/python3
"""
Adding a new state object to the database.
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
    lousiana = State(name="Lousiana")
    session.add(lousiana)
    session.commit()
    s = session.query(State).filter_by(name="Lousiana").first()
    if s:
        print(s.id)
    session.close()

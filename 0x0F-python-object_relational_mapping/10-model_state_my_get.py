#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ tate object with the name passed as argument from the database """
    engine = create_engine("""mysql+mysqldb://{}:{}@localhost/{}"""
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = (session.query(State).filter(State.name.like(argv[4])).first())
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()

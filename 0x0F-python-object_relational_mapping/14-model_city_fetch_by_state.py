#!/usr/bin/python3
""" Python file similar to model_state.py named model_city.py that contains the
    class definition of a City."""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ that prints all City objects from the database hbtn_0e_14_usa: """

    engine = create_engine("""mysql+mysqldb://{}:{}@localhost/{}"""
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    statesCities = (session.query(State, City).
                    filter(City.state_id == State.id).all())

    for state, city in statesCities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()

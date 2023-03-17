#!/usr/bin/python3
"""
script that lists all State objects, and corresponding City objects,
from the database hbtn_0e_100_usa via SQLAlchemy
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state_instance in session.query(State).order_by(State.id).all():
        for city_instance in state_instance.cities:
            print("{}: {} -> {}".format(city_instance.id, city_instance.name,
                                        state_instance.name))
    session.close()

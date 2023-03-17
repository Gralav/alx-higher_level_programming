#!/usr/bin/python3
"""
Start link class to table in database
"""
from sys import argv
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    engine = create_engine("""mysql+mysqldb://{}:{}@localhost/{}"""
                           .format(username, password, database_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).order_by(State.id.asc()).all()

    for row in result:
        print("{}: {}".format(row.id, row.name))
    session.close()

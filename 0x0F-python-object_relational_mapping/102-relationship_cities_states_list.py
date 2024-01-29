#!/usr/bin/python3
"""
lists all City objects from the database hbtn_0e_101_usa
Using relationship to access to the State object linked to the City object
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    states = session.query(State).order_by(State.id)
    for state in states:
        for city in state.cities:
            print(f'{city.id}: {city.name} -> {state.name}')
    session.close()

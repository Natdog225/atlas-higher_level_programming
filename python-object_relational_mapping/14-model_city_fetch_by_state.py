#!/usr/bin/python3
"""
This module defines a function that prints all City objects from
a database.
"""

import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)  # Create a Session class
    session = Session()                 # Create a session object

    for city in session.query(City).order_by(City.id).all():
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    session.close()

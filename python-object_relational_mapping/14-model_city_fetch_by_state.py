#!/usr/bin/python3
"""
This module defines a function that prints all City objects from
a database.
"""

import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Use a join to query both City and State
    for city, state in session.query(City, State) \
            .filter(City.state_id == State.id) \
            .order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()

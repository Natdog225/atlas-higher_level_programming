#!/usr/bin/python3
"""
This module defines a function that deletes all State objects with
a name containing the letter 'a' from a database.
"""

import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()
    for state in session.query(State).filter(State.name.like('%a%')):
        session.delete(state)
    session.commit()

    session.close()

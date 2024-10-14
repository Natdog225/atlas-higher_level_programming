#!/usr/bin/python3
"""
This module defines a function that lists all State objects that contain
the letter 'a' from a database.
"""

import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func  # Import func


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

    # Convert both the column and search string to lowercase
    for state in session.query(State).filter(
        func.lower(State.name).like('%a%')
    ).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    session.close()

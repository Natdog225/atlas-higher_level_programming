#!/usr/bin/python3
"""
Script to list all State objects that contain the letter a.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def filter_states_with_a():
    """
    Lists all State objects that contain the letter
    'a', sorted by states.id in ascending order.
    """

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ), pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).filter(
        State.name.like('%a%')
    ).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    filter_states_with_a()

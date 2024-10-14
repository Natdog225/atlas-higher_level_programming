#!/usr/bin/python3
"""
This module defines a function that lists all State objects that contain
the letter 'a' from a database.
"""

import sys
from model_state import Base, State

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

    # Use a case-insensitive SQL expression
    sql_query = """
        SELECT id, name
        FROM states
        WHERE name LIKE '%a%' COLLATE utf8mb4_general_ci
        ORDER BY id ASC;
    """
    result = session.execute(sql_query)

    for row in result:
        print("{}: {}".format(row[0], row[1]))

    session.close()

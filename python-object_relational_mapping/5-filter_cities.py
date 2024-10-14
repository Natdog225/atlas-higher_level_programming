#!/usr/bin/python3
"""
This module defines a function that lists all \
    cities from a given state in a database.
"""

import MySQLdb
from sys import argv


def filter_cities_by_state():
    """
    Lists all cities from the database hbtn_0e_4_usa for a given state.

    The script takes 4 arguments: mysql username, mysql password,
    database name, and state name.
    """

    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities \
                JOIN states ON cities.state_id = states.id \
                WHERE states.name = %s \
                ORDER BY cities.id ASC", (argv[4],))
    rows = cur.fetchall()

    # Extract city names and print them comma-separated
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    cur.close()
    db.close()


if __name__ == "__main__":
    filter_cities_by_state()

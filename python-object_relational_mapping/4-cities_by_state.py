#!/usr/bin/python3
"""
This module defines a function that lists all cities from a database.
"""

import MySQLdb
from sys import argv


def list_cities():
    """
    Lists all cities from the database hbtn_0e_4_usa.

    The script takes 3 arguments: mysql username, mysql password, and
    database name.
    """

    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities, states WHERE cities.state_id = states.id ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    list_cities()

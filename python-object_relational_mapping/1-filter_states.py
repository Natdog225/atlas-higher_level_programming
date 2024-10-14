#!/usr/bin/python3
"""
This module defines a function that lists all states with a name
starting with N from a database.
"""

import MySQLdb
from sys import argv


def filter_states():
    """
    Lists all states with a name starting with N from the
    database hbtn_0e_0_usa.

    The script takes 3 arguments: mysql username, mysql password, and
    database name.
    """

    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states()

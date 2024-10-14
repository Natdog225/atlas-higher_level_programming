#!/usr/bin/python3
"""
This module defines a function that lists all states from a database.
"""

import MySQLdb
from sys import argv


def list_states():
    """
    Lists all states from the database hbtn_0e_0_usa.

    The script takes 3 arguments: mysql username, mysql password, and
    database name.
    """

    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    list_states()

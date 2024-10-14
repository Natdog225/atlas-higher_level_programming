#!/usr/bin/python3
"""
This module defines a function that lists all states matching
a given name from a database, protected from MySQL injections.
"""

import MySQLdb
from sys import argv


def filter_states_by_name_safe():
    """
    Lists all states with a name matching the argument from the
    database hbtn_0e_0_usa, safe from MySQL injections.

    The script takes 4 arguments: mysql username, mysql password,
    database name, and state name searched.
    """

    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states_by_name_safe()

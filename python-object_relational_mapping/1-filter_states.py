#!/usr/bin/python3
"""Write a script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """including the guard clause"""

    """connection to the MySQLdb database"""
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3])

    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE states.name "
        "LIKE BINARY 'N%' ORDER BY states.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connection.close()

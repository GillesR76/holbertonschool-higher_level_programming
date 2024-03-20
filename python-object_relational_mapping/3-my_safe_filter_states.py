#!/usr/bin/python3
"""script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument, one that is
safe from MySQL injections
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
    cmd = "SELECT * FROM states WHERE states.name = %s ORDER BY states.id"
    cursor.execute(cmd, (sys.argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connection.close()

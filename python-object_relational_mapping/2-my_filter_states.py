#!/usr/bin/python3


"""Write a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
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
        "SELECT * FROM states WHERE states.name LIKE BINARY "
        "'{}' ORDER BY states.id".format(sys.argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connection.close()

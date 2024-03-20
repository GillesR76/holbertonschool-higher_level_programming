#!/usr/bin/python3
""" script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys
import os

username = os.getenv('DB_USER')
password = os.getenv('DB_PASS')
database = os.getenv('DB_NAME')


if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    cursor = connection.cursor()
    cmd = ("SELECT cities.name FROM cities "
           "INNER JOIN states ON cities.state_id = states.id "
           "WHERE states.name = %s ORDER BY cities.id")
    cursor.execute(cmd, (sys.argv[4],))

    rows = cursor.fetchall()
    to_string = ', '.join(map(" ".join, rows))
    print(to_string)

    connection.close()

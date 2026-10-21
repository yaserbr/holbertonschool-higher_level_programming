#!/usr/bin/python3
"""List all states from a MySQL database."""

import MySQLdb
import sys

if __name__ == "__main__":
    myconnection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8",
    )

    cursor = myconnection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    myconnection.close()

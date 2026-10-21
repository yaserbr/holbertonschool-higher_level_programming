#!/usr/bin/python3
"""This module lists all states from a MySQL database."""

import MySQLdb
import sys

if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8",
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    connection.close()

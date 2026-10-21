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
c = connection.cursor()
c.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
for data in c.fetchall():
    print(data)
c.close()
connection.close()

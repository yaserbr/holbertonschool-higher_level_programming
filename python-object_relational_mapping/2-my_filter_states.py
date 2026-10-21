#!/usr/bin/python3
"""List all states whose names start with an uppercase N."""

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
    target = sys.argv[4]

    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM states "
        "WHERE BINARY name LIKE '{}' "
        "ORDER BY states.id ASC".format(target)
    )

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    connection.close()

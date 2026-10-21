#!/usr/bin/python3
"""List states matching a user-provided name safely."""

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

    query = (
        "SELECT * FROM states "
        "WHERE BINARY name = %s "
        "ORDER BY states.id ASC"
    )

    cursor = connection.cursor()
    cursor.execute(query, (target,))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    connection.close()

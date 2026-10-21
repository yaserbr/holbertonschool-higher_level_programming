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
    query = (
        "SELECT cities.name, cities.id,states.name FROM cities "
        "INNER JOIN states "
        "ON cities.state_id = states.id "
    )

    cursor = connection.cursor()
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    connection.close()

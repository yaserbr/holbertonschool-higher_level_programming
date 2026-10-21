#!/usr/bin/python3
"""List all cities belonging to a given state."""

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
        "SELECT cities.name "
        "FROM cities "
        "INNER JOIN states "
        "ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )

    cursor = connection.cursor()
    cursor.execute(query, (sys.argv[4],))

    cities = cursor.fetchall()
    names = [city[0] for city in cities]

    print(", ".join(names))

    cursor.close()
    connection.close()

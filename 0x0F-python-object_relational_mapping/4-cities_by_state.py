#!/usr/bin/python3
"""filter states script"""

import sys
import MySQLdb

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    host = "localhost"

    cnx = MySQLdb.connect(
        host=host,
        user=username,
        passwd=password,
        db=database
    )

    cur = cnx.cursor()
    sql = """
    SELECT cities.id AS id, cities.name AS name, states.name AS state_name
    FROM states INNER JOIN cities ON states.id = cities.state_id
    ORDER BY cities.id ASC
    """
    cur.execute(sql)

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    cnx.close()

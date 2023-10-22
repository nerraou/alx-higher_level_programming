#!/usr/bin/python3
"""filter states script"""

import sys
import MySQLdb

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]
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
    WHERE state.name LIKE %s
    COLLATE utf8mb4_bin
    ORDER BY cities.id ASC
    """
    cur.execute(sql, (name,))

    flag = False
    query_rows = cur.fetchall()
    for row in query_rows:
        if flag is True:
            print(", ")
        flag = True
        print("{}".format(row[1]))

    cur.close()
    cnx.close()

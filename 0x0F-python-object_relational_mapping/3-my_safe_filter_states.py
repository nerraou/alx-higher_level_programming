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
    SELECT *
    FROM states
    WHERE name LIKE %s
    COLLATE utf8mb4_bin
    ORDER BY id ASC
    """
    cur.execute(sql, name)

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    cnx.close()

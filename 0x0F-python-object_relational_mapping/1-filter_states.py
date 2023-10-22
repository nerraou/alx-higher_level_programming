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
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    cnx.close()

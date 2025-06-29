#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument.
Usage: ./2-my_filter_states.py <mysql username> <mysql password> <database name> <state name searched>
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )

    cur = db.cursor()
    # Use exact match and prevent SQL injection
        cur.execute("""SELECT * FROM states
                 WHERE BINARY name LIKE '{}%'
                 ORDER BY id;""".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()

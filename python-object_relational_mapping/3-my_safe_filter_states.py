#!/usr/bin/python3
"""Safely filters states by name using parameterized query"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Read arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    # Create cursor and execute safe query
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))

    # Print results
    for row in cur.fetchall():
        print(row)

    # Cleanup
    cur.close()
    db.close()

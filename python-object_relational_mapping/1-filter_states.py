#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Arguments: username, password, db name
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor and execute query
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch and print results
    for row in cur.fetchall():
        print(row)

    # Close
    cur.close()
    db.close()

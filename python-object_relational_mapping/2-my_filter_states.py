#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa where name matches the user input.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Read MySQL credentials and target state name from arguments
    username, password, database, state_name = sys.argv[1:5]

    # Connect to MySQL server on localhost:3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    # Build and execute query using string formatting (not SQL injection safe)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    # Display the query results
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()

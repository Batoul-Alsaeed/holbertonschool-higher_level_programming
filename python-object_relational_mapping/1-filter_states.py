#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
that start with the letter 'N' (uppercase only).
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server on localhost, port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute SQL query to select states that start with 'N', sorted by id
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all matching rows
    rows = cursor.fetchall()

    # Print each row in the required format
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

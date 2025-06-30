#!/usr/bin/python3
"""
3-my_safe_filter_states.py

Safe script to filter states in the hbtn_0e_0_usa database without risking SQL injection.
Takes four arguments: mysql username, mysql password, database name, and state name to search.
Displays matching records sorted by id.
"""

import MySQLdb
import sys


def main():
    """Main function: connects to db, performs parameterized query, prints results."""
    username, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()

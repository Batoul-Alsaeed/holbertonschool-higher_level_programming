#!/usr/bin/python3
"""
Module that lists all states from the database hbtn_0e_0_usa
safely filtering by name using parameterized query (case-sensitive)
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cursor = db.cursor()
    cursor.execute("SELECT * \
    FROM states \
    WHERE CONVERT(`name` USING Latin1) \
    COLLATE Latin1_General_CS = %s ORDER BY id ASC;", (sys.argv[4],))
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()

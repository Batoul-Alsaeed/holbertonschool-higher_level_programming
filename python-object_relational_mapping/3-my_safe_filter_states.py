#!/usr/bin/python3
"""
Safely displays all values in the states table where name matches the user input.
Prevents SQL injection by using parameterized queries.
Usage: ./3-my_safe_filter_states.py <mysql username> <mysql password> <database name> <state name searched>
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    connexion = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    argv_4 = argv[4].split(';')[0]

    curs = connexion.cursor()
    curs.execute("""SELECT * FROM states
                 WHERE BINARY name LIKE '{}%'
                 ORDER BY id;""".format(argv_4))
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    connexion.close()

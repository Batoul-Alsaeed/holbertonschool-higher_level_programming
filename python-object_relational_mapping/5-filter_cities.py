#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa
Safely filters using parameterized query to avoid SQL injection
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=username, passwd=password, db=db_name
    )

    cur = db.cursor()
    cur.execute("""
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (state_name,))

    rows = cur.fetchall()
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    cur.close()
    db.close()

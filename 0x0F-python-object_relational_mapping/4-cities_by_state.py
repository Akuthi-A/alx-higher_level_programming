#!/usr/bin/python3

"""
 lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    uname = sys.argv[1]
    pwd = sys.argv[2]
    dbase = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=uname, password=pwd, db=dbase)

    cursor = conn.cursor()

    query = "SELECT cities.id, cities.name, states.name FROM cities, states WHERE cities.state_id = states.id;"
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()

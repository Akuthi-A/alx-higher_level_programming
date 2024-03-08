#!/usr/bin/python3

"""
a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    uname = sys.argv[1]
    pwd = sys.argv[2]
    dbase = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=uname, password=pwd, db=dbase)

    cursor = conn.cursor()

    cursor.execute("""SELECT name FROM cities WHERE (SELECT id FROM states WHERE
                BINARY name = %s) = state_id""", (sys.argv[4],))

    rows = cursor.fetchall()

    print(", ".join([row[0] for row in rows]))

    cursor.close()
    conn.close()

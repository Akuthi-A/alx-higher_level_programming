#!/usr/bin/python3

"""
 a script that takes in an argument and
  displays all values in the states table of 
  hbtn_0e_0_usa where name matches the argument
  safe from SQL injection
"""

import MySQLdb
import sys


if __name__ == "__main__":
    uname = sys.argv[1]
    pwd = sys.argv[2]
    dbase = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=uname, passwd=pwd, db=dbase)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC", (sys.argv[4],))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()

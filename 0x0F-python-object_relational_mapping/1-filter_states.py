#!/usr/bin/python3

"""
lists all states with a name starting with N (upper N) 
from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    uname = sys.argv[1]
    pwd = sys.argv[2]
    dbase = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=uname, passwd=pwd, db=dbase)

    cursor = conn.cursor()

    query = """
        SELECT * FROM states WHERE name LIKE BINARY 'N%'
        ORDER BY id ASC
        """
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()

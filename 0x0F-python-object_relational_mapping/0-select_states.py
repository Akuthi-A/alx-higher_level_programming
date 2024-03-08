#!/usr/bin/python3

"""

python script that lists database contents of a table

"""



import MySQLdb

import sys





if __name__ == "__main__":

    uname = sys.argv[1]

    password = sys.argv[2]

    dbase = sys.argv[3]



    conn = MySQLdb.connect(host="localhost", port=3306, user=uname, password=password, database=dbase)



    cursor = conn.cursor()



    query = "SELECT * FROM states ORDER BY id ASC"

    cursor.execute(query)



    rows = cursor.fetchall()



    for row in rows:

        print(row)



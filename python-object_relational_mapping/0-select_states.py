#!/usr/bin/env python3
"""list states in databse"""
import MySQLdb
import sys


def list_states(username, password, dbname):
    """connects to mysql database"""
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         password=password,
                         db=dbname)

    # create a cursor object
    cursor = db.cursor()

    # execute the sql query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # fetch all the rows
    rows = cursor.fetchall()

    # print each row
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    # get command line arg
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # call the function to list states
    list_states(username, password, dbname)

#!/usr/bin/env python3
import MySQLdb
import sys

if __name__ == "__main__":
    # get mysql credentials and database name from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # connecting to server...
    db = MySQLdb.connect(
    host='localhost',
    port=3306,
    user=mysql_username,
    passwd=mysql_password,
    db=database_name
    )

    # cursor object to interact with the database
    cursor = db.cursor()

    # execute the sql query to list all states in asc order by id
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

    # fetch all the rows returned by the query
    rows = cursor.fetchall()

    # print each row
    for row in rows:
        print(row)
    
    # close the cursor and database
    cursor.close()
    db.close()
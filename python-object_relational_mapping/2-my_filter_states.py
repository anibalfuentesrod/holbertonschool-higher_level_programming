#!/usr/bin/python3
"""filter the states by the name givn in the chmod thing"""
import sys
import MySQLdb

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the mysql server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname,
        charset="utf8"
    )

    # Create cursor obj
    cursor = db.cursor()

    # sql query
    query = """SELECT * FROM states WHERE name LIKE BINARY '{}' \
        ORDER BY states.id ASC"""
    query = query.format(state_name)
    # execute the query
    cursor.execute(query)

    # fetch results
    states = cursor.fetchall()

    # using for loop to print the resutls
    for state in states:
        print(state)

    # close cursor and connection
    cursor.close()
    db.close()

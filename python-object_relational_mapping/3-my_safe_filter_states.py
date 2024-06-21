#!/usr/bin/python3
"""Fetch states from the database safely"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> \
              <mysql password> <database name> \
              <state name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    # Establish a connection to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname,
        charset="utf8"
    )

    # Create a cursor to execute SQL queries
    cursor = db.cursor()

    # Prepare the SQL query using placeholders to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the query, safely passing the user input
    cursor.execute(query, (state_name,))

    # Retrieve all rows from the executed query
    states = cursor.fetchall()

    # Display the fetched states
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()

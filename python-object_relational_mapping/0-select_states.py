#!/usr/bin/env python3
import MySQLdb
import sys


def list_users(username, password):
    """Connects to MySQL database and lists all users"""
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db="mysql",  # Connect to the 'mysql' database
                         port=3306)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query to list all users
    cursor.execute("SELECT user, host FROM user")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Call the function to list users
    list_users(username, password)

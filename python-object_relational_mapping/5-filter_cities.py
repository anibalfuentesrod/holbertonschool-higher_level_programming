#!/usr/bin/python3
"""lists all cities of the states in database hbt..."""
import MySQLdb
import sys

if __name__ == "__main__":
    # check command line arguments
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> \
              <mysql password> \
              <database name> \
              <state name>".format(sys.argv[0]))
        sys.exit(1)

    # get the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    # connect to mysql db
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=dbname,
                         port=3306)

    # create cursor onj to be able to execute query's
    cursor = db.cursor()

    # query = list all cities by ascended order
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # fetch and print
    cities = cursor.fetchall()
    print(", ".join(city[0] for city in cities))

    # close cursor and database connection too
    cursor.close()
    db.close()

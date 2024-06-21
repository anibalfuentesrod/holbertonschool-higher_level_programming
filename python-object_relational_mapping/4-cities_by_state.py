#!/usr/bin/python3
"""list all the cities in database htb..."""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> \
              <mysql password> \
              <database name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # connect to mysql
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname,
        charset="utf8"
    )

    # create cursor obj
    cursor = db.cursor()

    # sql query
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """

    # execute the query on top of this
    cursor.execute(query)

    # gives the result using fetchall()
    cities = cursor.fetchall()

    # prints the results using a for loop to iterate over it
    for city in cities:
        print(city)

    # close cursor and connection
    cursor.close()
    db.close()

#!/usr/bin/python3
"""list states in database hbt..."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # get mysql username, password, and database name
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # create engine to connect to mysql server
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}',
        pool_pre_ping=True
    )
    # create a config session class
    Session = sessionmaker(bind=engine)

    # now create the session
    session = Session()

    # query all states in order by id
    states = session.query(State).order_by(State.id).all()

    # print each state using a for loop
    for state in states:
        print(f"{state.id}: {state.name}")

    # close the session
    session.close()

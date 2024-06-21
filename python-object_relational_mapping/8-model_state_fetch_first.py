#!/usr/bin/python3
"""print the first state in database hbt..."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # get the sql username, password, and database name
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # create engine to connect to server
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}',
        pool_pre_ping=True
    )

    # create a configured session class
    Session = sessionmaker(bind=engine)

    # create the session
    session = Session()

    # query the first state obj by id
    state = session.query(State).order_by(State.id).first()

    # prints the first state if not it will print 'nothing'
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    # close the session
    session.close()

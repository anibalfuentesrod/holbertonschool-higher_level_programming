#!/usr/bin/python3
"""script that list all the states containing the letter 'a'"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # get credentials and the db name ffrom command line
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # create a engine to bind to the session
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # query all states containing the letter 'a' in order by id
    states = session.query(State).filter(State.name.like('%a%')).order_by(
        State.id.asc()).all()

    # print the results using a for loop
    for state in states:
        print(f"{state.id}: {state.name}")

    # close the session
    session.close()

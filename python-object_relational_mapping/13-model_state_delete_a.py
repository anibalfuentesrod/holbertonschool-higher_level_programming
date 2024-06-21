#!/usr/bin/python3
"""script that deletes all states containing letter 'a'"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # get sql credentials and dbname in command line
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # create engine and then bind it to session
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # query and del all states obj that have letter 'a'
    states_to_delete = session.query(State).filter(
        State.name.contains('a')).all()
    # iterates trhough to deleted with a for loop
    for state in states_to_delete:
        session.delete(state)
    session.commit()

    # close the session
    session.close()

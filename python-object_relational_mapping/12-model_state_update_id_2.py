#!/usr/bin/python3
"""sript that udpdates the name of state, id = 2 <- that one"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # get sql credentials and dbname ffrom command line
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # create new engine to bind to session
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # query the States obj by id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # updates the states name
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # close the session
    session.close()

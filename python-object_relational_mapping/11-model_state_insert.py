#!/usr/bin/python3
"""script that adds new stateee hahaha let's goo"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # get credentials, ffrom mysql and dbname from command line
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # create engine to bind to session
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # create new session obj
    new_state = State(name="Louisiana")

    # adds the new state to session
    session.add(new_state)
    session.commit()

    # prints the new sessions id
    print(new_state.id)

    # close the session
    session.close()

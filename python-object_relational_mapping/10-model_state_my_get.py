#!/usr/bin/python3
"""Script to get a State object by name from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    # Create the engine and bind it to the session
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the state with the given name
    state = session.query(State).filter(State.name == state_name).first()

    # Print the result
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    # Close the session
    session.close()

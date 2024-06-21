#!/usr/bin/python3
"""script that list all states on database hbtn_0e_14_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    # get mysql credentials and dbname ffrom command line
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # create an engine and bind it to session
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # query all city obj and join to state obj order by cities.id
    results = session.query(City, State).join(State).order_by(City.id).all()

    # prints the result using a for loop to iterate throught
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    # close the session
    session.close()

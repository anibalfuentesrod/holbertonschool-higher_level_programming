#!/usr/bin/python3
"""list states in database"""
import MySQLdb
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """base of the sql"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)


def list_states(username, password, dbname):
    """connects to mysql database"""
    # create a connection string
    conn_str = f"mysql+mysqldb://{username}:{password}@localhost/{dbname}"

    # create an engine
    engine = create_engine(conn_str)

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()

    # query all states and order by id
    states = session.query(State).order_by(State.id.asc()).all()

    # print each state
    for state in states:
        print(f"({state.id}, '{state.name}')")

    session.close()


if __name__ == "__main__":
    # get command line arg
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # call the function to list states
    list_states(username, password, dbname)

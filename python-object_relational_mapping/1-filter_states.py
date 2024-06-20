#!/usr/bin/python3
"""list all states that start with the letter N"""
import MySQLdb
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """class represents the states of table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)


def states_with_n(username, password, dbname):
    """connect mysql db and list states with n"""
    # create a connection str
    conn_str = f"mysql+mysqldb://{username}:{password}@localhost/{dbname}"

    # create an engine
    engine = create_engine(conn_str)

    # create a config "session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # query states with starting letter N and order by id
    states = session.query(State).filter(
        State.name.like('N%')).order_by(
            State.id.asc()).all()

    # print each state
    for state in states:
        print(f"({state.id}, '{state.name}')")

    session.close()


if __name__ == "__main__":
    # get the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # call the func to list states with the letter N
    states_with_n(username, password, dbname)

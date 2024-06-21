#!/usr/bin/python3
"""filters the usr input to match the state"""
import MySQLdb
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """state class representing state table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)


def filter_states(username, password, dbname, state_name):
    """connect to mysql db and filter states, se deja llevar del user input"""
    # conectando
    conn_str = f"mysql+mysqldb://{username}:{password}@localhost/{dbname}"

    # empieza engine(crear)
    engine = create_engine(conn_str)

    # creando una session class
    Session = sessionmaker(bind=engine)

    # crea session
    session = Session()

    # esta es la linea de codigo q filtra en user input y compara
    states = session.query(State).filter(
        State.name == state_name
    ).order_by(State.id.asc()).all()

    # printea los states iterando por cada uno con un for loop
    for state in states:
        print(f"({state.id}, '{state.name}')")

    # cerrando la session duhh
    session.close()


if __name__ == "__main__":
    """Command line argument"""
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    filter_states(username, password, dbname, state_name)

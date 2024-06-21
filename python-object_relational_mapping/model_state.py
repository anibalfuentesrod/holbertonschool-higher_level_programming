#!/usr/bin/python3
"""models base let's gooo"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# create base class using the function declarative_base()
Base = declarative_base()


class State(Base):
    """states class that links to 'states' in mysql server"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

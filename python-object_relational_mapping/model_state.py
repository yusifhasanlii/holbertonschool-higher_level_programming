#!/usr/bin/python3
"""
Contains the class definition of a State and an instance
Base = declarative_base().
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that links to the MySQL table states.

    Attributes:
        id (int): The state's id (Primary Key).
        name (str): The state's name.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

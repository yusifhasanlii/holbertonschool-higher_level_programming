#!/usr/bin/python3
"""
Prints the State object with the name passed as argument.
Safe from SQL injections using SQLAlchemy.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Create the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query: Search by the name provided as an argument
    # Using .first() because we expect one result
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # If the state exists, print its ID, otherwise print "Not found"
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    # Close the session
    session.close()

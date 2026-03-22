#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa.
Updates the state where id = 2 to 'New Mexico'.
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

    # Find the object with ID 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # If the object is found, change its name and commit
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()

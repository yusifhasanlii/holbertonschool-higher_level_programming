#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a' from the database.
Sorted in ascending order by states.id.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Engine yaradılır
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Session yaradılır
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query: Adında 'a' hərfi olanları id üzrə artan sıra ilə götürürük
    states = session.query(State).filter(State.name.like('%a%')) \
                                 .order_by(State.id).all()

    # Nəticələri çap edirik
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Session bağlanır
    session.close()

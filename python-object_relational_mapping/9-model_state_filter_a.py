#!/usr/bin/python3
"""Print all State objects containing the letter 'a' from the database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connect to the database
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query states with 'a' in their name
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Print each result
    for state in states:
        print(f"{state.id}: {state.name}")

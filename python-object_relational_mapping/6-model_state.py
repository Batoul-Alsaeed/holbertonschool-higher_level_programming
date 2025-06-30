#!/usr/bin/python3
"""Create the states table in the database using SQLAlchemy"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    # Create connection to MySQL database
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}",
        pool_pre_ping=True
    )

    # Create tables defined by Base subclasses
    Base.metadata.create_all(engine)

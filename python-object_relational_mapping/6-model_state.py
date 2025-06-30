#!/usr/bin/python3
"""
Creates 'states' table using SQLAlchemy
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    # connect to database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # create tables from models
    Base.metadata.create_all(engine)

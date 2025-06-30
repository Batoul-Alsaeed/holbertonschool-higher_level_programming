#!/usr/bin/python3
"""Fetch all cities and their states from DB"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Setup engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Join states and cities and sort by city.id
    results = session.query(City, State).join(State).order_by(City.id).all()
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

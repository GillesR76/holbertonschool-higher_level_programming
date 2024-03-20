#!/usr/bin/python3


"""write a script 14-model_city_fetch_by_state.py that
prints all City objects from the database hbtn_0e_14_usa
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import Base, State
import sys


if __name__ == "__main__":
    """including the guard clause"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    """creating a SQLAlchemy engine that will connect to the MySQL database"""

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Printing all city objects from the database and joining
    both cities and state objects in order to print information
    from both objects
    """
    for cities, states in (session.query(City, State)
                           .join(State, City.state_id == State.id)
                           .order_by(City.id)):
        print(f"{states.name}: ({cities.id}) {cities.name}")

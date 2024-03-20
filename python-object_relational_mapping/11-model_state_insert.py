#!/usr/bin/python3


"""Write a script that adds the State object
Louisiana to the database hbtn_0e_6_usa
"""


from sqlalchemy import create_engine, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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

    """ Adding a state into the state table by first
    creating a new state object, then adding the object
    to the session and commiting the changes to the database
    """
    add_state = State(name='Louisiana')
    session.add(add_state)
    session.commit()
    print(add_state.id)
    session.close()

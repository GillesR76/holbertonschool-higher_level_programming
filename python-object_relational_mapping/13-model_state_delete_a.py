#!/usr/bin/python3


"""Write a script that deletes all State objects with a
name containing the letter a from the database hbtn_0e_6_usa
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

    """ Deleting state objects containing the letter a
    using the filter and delete and committing the changes
    to the database
    """
    session.query(State).filter(State.name.like('%a%')).delete()
    session.commit()
    session.close()

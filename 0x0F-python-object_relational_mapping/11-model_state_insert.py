#!/usr/bin/python3
"""
A script get first state
"""

import sys
from model_state import State
from sqlalchemy import create_engine, orm

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database)

    engine = create_engine(db_url)

    session = orm.Session(engine)

    state = State(name="Louisiana")

    session.add(state)
    session.commit()
    session.close()

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

    states = session.query(State).\
        order_by(State.id).filter(State.name.contains("a"))
    for instance in states:
        print('{}: {}'.format(instance.id, instance.name))

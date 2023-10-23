#!/usr/bin/python3
"""
A script get first state
"""

import sys
from model_state import State
from model_city import City
from sqlalchemy import create_engine, orm

if __name__ == "__main__":
    """
    Access to the database and get the states and cities
    from the database.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database)

    engine = create_engine(db_url)

    session = orm.Session(engine)

    rows = session.query(City, State).join(State)
    for city, state in rows.all():
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    session.close()

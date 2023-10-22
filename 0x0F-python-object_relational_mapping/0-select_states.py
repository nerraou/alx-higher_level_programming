#!/usr/bin/python3
"""select states script"""

import sys
import sqlalchemy
from sqlalchemy import orm

if __name__ == "__main__":
    metadata = sqlalchemy.MetaData()

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    idCol = sqlalchemy.Column('id', sqlalchemy.Integer(), primary_key=True)
    nameCol = sqlalchemy.Column('name', sqlalchemy.String(256), nullable=False)
    State = sqlalchemy.Table('states', metadata, idCol, nameCol)

    format_str = 'mysql+mysqldb://{}:{}@localhost/{}'
    connection_string = format_str.format(username, password, database)
    engine = sqlalchemy.create_engine(connection_string, pool_pre_ping=True)

    session = orm.Session(engine)
    for state in session.query(State).order_by(State.c.id).all():
        print("({}, {})".format(state.id, state.name))
    session.close()

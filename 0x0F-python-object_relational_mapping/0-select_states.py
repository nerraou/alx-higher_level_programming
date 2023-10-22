#!/usr/bin/python3

import sys
from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base

Base = orm.declarative_base()

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database), pool_pre_ping=True)
Base.metadata.create_all(engine)

# Base.metadata.create_all(engine)

# session = Session(engine)
# for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
#     print("{}: {}".format(state.id, state.name))
# session.close()


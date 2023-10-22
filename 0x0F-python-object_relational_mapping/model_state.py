#!/usr/bin/python3
"""
the class definition of a State and
an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, orm

Base = orm.declarative_base()


class State(Base):
    """
    State class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

#!/usr/bin/python3
"""Base class module"""

from json import dumps


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Base class constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """serilize list of dictionaries to json string"""
        if list_dictionaries is None:
            return "[]"
        return dumps(list_dictionaries)

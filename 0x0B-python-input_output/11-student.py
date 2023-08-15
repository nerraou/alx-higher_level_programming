#!/usr/bin/python3
"""
class student
"""


class Student:
    """
    class student
    """
    def __init__(self, first_name, last_name, age):
        """
        init student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrives dictionary representation
        """
        res = {}
        if type(attrs) is list:
            for key in attrs:
                if key in self.__dict__:
                    res[key] = self.__dict__[key]
            return res
        return self.__dict__

    def reload_from_json(self, json):
        """
        reload from json
        """
        if not json:
            return
        self.__dict__ = json

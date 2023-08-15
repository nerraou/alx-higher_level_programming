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
        if attrs is not None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return res
        return self.__dict__

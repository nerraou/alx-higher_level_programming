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
            lst3 = {value for value in attrs if value in self.__dict__}
            return lst3
        return self.__dict__

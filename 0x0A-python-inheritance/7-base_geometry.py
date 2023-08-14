#!/usr/bin/python3
"""
BaseGeometry
"""


class BaseGeometry:
    """
    Base Geometry class
    """
    def area(self):
        """
        usless area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        int validator
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

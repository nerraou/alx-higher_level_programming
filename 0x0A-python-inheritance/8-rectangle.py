#!/usr/bin/python3
"""
BaseGeometry
"""


class BaseGeometry:
    """
    Base Geometry class
    """
    def __init__(self, width, height):
        """ init geometry"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width

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

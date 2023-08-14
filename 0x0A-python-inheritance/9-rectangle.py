#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle
    """
    def __init__(self, width, height):
        """ init geometry"""
        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width

    def area(self):
        """ calculate rectangle area """
        return self.__width * self.__height

    def __str__(self):
        """ return str representation """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

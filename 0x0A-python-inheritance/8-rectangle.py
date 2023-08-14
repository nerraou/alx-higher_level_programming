#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    REctangle
    """
    def __init__(self, width, height):
        """ init geometry"""
        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width

#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square
    """
    def __init__(self, size):
        """ init Square"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ calculate Square area """
        return self.__size ** 2

    def __str__(self):
        """square str """
        return "[Square] {}/{}".format(self.__size, self.__size)

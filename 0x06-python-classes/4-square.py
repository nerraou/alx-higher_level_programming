#!/usr/bin/python3
"""Square class"""


class Square:
    """square class with private size attribute"""
    __size = None

    def __init__(self, size=0):
        """Initializes size attribute."""
        self.__validate_size(size)
        self.__size = size

    def area(self):
        """calculate the area of the square"""
        return self.__size * self.__size

    def size(self):
        """return size attribute"""
        return self.__size

    def size(self, value):
        self.__validate_size(size)
        self.__size = value

    def __validate_size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

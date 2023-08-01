#!/usr/bin/python3
"""Square class"""


class Square:
    """square class with private size attribute"""
    __size = None

    def __init__(self, size=0):
        """Initializes size attribute."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculate the area of the square"""
        return self.__size * self.__size

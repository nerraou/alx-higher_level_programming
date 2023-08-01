#!/usr/bin/python3
"""Square class"""


class Square:
    """square class with private size attribute"""
    __size = None
    __position = None

    def __init__(self, size=0, position=(0, 0)):
        """Initializes size attribute."""
        self.size = size
        self.position = position

    def __str__(self):
        """return square prints"""
        if self.size == 0:
            return "\n"
        str = "\n" * self.position[1]
        for i in range(0, self.size):
            str += " " * self.position[0] + "#" * self.size + "\n"
        return str

    def area(self):
        """calculate the area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        """get size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size attribute"""
        self.__validate_size(value)
        self.__size = value

    @property
    def position(self):
        """get postion"""
        return self.__position

    @position.setter
    def position(self, value):
        """set position"""
        self.__validate_position(value)
        self.__position = value

    def my_print(self):
        """print the square"""
        print(self, end="")

    def __validate_size(self, value):
        """validate size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def __validate_position(self, value):
        """validate position"""
        if (type(value) != tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (len(value) != 2 or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

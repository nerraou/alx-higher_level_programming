#!/usr/bin/python3
"""Square class"""


class Square:
    """square class with private size attribute"""
    __size = None

    def __init__(self, size=0):
        """Initializes size attribute."""
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        self.__size = new_size

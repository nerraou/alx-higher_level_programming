#!/usr/bin/python3
"""Square class"""

class Square:
    """square class with private size attribute"""
    __size = None

    def __init__(self, new_size):
        """Initializes size attribute."""
        self.__size = new_size

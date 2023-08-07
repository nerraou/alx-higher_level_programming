#!/usr/bin/python3
"""RECTANGLE"""


class Rectangle:
    """
    This is rectangle empty class
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        """calculate area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """calculate perimeter of rectangle"""
        if self.__width == 0 or self.height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        rectangle = []
        """REturn the rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append("#")
            rectangle.append("\n")
        rectangle.pop()
        return "".join(rectangle)

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, width):
        """set width value"""
        self.__validate_width(width)
        self.__width = width

    def __validate_width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set height value"""
        self.__validate_height(height)
        self.__height = height

    def __validate_height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

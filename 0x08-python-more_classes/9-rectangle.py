#!/usr/bin/python3
"""RECTANGLE"""


class Rectangle:
    """
    This is rectangle empty class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init rectangle"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """delete rectangle"""
        print("{:s}".format("Bye rectangle..."))
        type(self).number_of_instances -= 1

    @classmethod
    def square(cls, size=0):
        """
        returns a new Rectangle instance with width == height == size
        """
        return Rectangle(size, size)

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
        """Return the rectangle with print_symbol"""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append(str(self.print_symbol))
            rectangle.append("\n")
        rectangle.pop()
        return "".join(rectangle)

    def __repr__(self):
        """return a string representation
        of the rectangle to be able
        to recreate a new instance by using eval()
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        static method return the
        that returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        rec1 = rect_1.area()
        rec2 = rect_2.area()

        if rec1 >= rec2:
            return rect_1
        return rect_2

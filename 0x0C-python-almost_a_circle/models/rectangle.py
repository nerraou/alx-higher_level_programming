#!/usr/bin/python3
"""Rectangle class module"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class constructor"""

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """calculate rectangle area"""
        return self.width * self.height

    def display(self):
        """display rectangle"""
        empty_rows = "\n" * self.y
        row = " " * self.x + "#" * self.width
        row += "\n"

        if (len(empty_rows) >= 1):
            print(empty_rows, end="")
        print(row * self.height, end="")

    def update(self, *args, **kwargs):
        """update rectangle"""

        if args is None or len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

        if (args is None):
            return

        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) == 5:
            self.y = args[4]

    def to_dictionary(self):
        """return dictionary representation"""
        return {"x": self.x, "y": self.y, "id": self.id,
                "height": self.height, "width": self.width}

    def __str__(self):
        """Rectangle string respresentation"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    @property
    def width(self):
        """width attribute getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width attribute setter"""
        self.__validate_integer("width", width)
        self.__validate_gt_zero("width", width)
        self.__width = width

    @property
    def height(self):
        """height attribute getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height attribute setter"""
        self.__validate_integer("height", height)
        self.__validate_gt_zero("height", height)
        self.__height = height

    @property
    def x(self):
        """x attribute getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x attribute setter"""
        self.__validate_integer("x", x)
        self.__validate_ge_zero("x", x)
        self.__x = x

    @property
    def y(self):
        """y attribute getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y attribute setter"""
        self.__validate_integer("y", y)
        self.__validate_ge_zero("y", y)
        self.__y = y

    def __validate_integer(self, attribute, value):
        """validate integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attribute))

    def __validate_gt_zero(self, attribute, value):
        """validate greater than zero"""
        if value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    def __validate_ge_zero(self, attribute, value):
        """validate greater than or eqaul zero"""
        if value < 0:
            raise ValueError("{} must be >= 0".format(attribute))

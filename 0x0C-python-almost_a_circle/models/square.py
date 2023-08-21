#!/usr/bin/python3
"""Rectangle class module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Square class constructor"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Square string respresentation"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def update(self, *args, **kwargs):
        """update square"""

        if args is None or len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

        if (args is None):
            return

        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) == 4:
            self.y = args[3]

    def to_dictionary(self):
        """return dictionary representation"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    @property
    def size(self):
        """size attribute getter"""
        return self.width

    @size.setter
    def size(self, size):
        """size attribute setter"""
        self.width = size
        self.height = size

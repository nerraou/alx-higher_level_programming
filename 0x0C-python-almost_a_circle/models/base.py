#!/usr/bin/python3
"""Base class module"""


from json import dumps, loads, load

class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Base class constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """serilize list of dictionaries to json string"""
        if list_dictionaries is None:
            return "[]"
        return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """from json string"""
        if json_string is None or len(json_string) == 0:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create class from dictionary"""
        from models.rectangle import Rectangle
        from models.square import Square

        instance = None
        if cls.__name__ == "Rectangle":
            instance = Rectangle(4, 3)
        if cls.__name__ == "Square":
            instance = Square(10)

        if instance is not None:
            instance.update(**dictionary)
        return instance

    @classmethod
    def save_to_file(cls, list_objs):
        """serilize list of dictionaries to json file"""
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as f:
            list_dictionaries = [obj.to_dictionary() for obj in list_objs]
            f.write(Base.to_json_string(list_dictionaries))

    @classmethod
    def load_from_file(cls):
        """load from file"""

        try:
            filename = "{}.json".format(cls.__name__)
            objects =  []
            with open(filename, "r") as f:
                objects_json = cls.from_json_string(f.read())
                for obj in objects_json:
                    objects.append(cls.create(**obj))
            return objects
        except FileNotFoundError:
            return []

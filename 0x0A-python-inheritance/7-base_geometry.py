#!/usr/bin/python3
""" 7-base_geometry: class BaseGeometry """


class BaseGeometry:
    """
        class BaseGeometry
    """

    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value

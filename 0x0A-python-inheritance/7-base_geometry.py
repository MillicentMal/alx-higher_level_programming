#!/usr/bin/python3
""" 5-base_geometry: class BaseGeometry """


class BaseGeometry:
    """
        class BaseGeometry
    """
    def __init__(self):
        pass
    
    def area(self):
        raise "area() is not implemented"
    
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value <= 0:
            raise ValueError("value must be greater than 0")
        

        
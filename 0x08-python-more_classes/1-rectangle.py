#!/usr/bin/python3
"""Defines a class of a rectangle
"""


class Rectangle:
    """Rectangle class"""
    
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self): 
        return self.__width

    @width.setter
    def width(self, value):
        try:
            self.__width = value
        except TypeError:
            if not isinstance(value, int):
                print("value must be an integer")
        except ValueError:
            if value < 0:
                print("value must be >= 0")
        

    @property
    def height(self):
         return self.__height

    @height.setter
    def height(self, value):
        try:
            self.__height = value
        except TypeError:
            if not isinstance(value, int):
                print("value must be an integer")
        except ValueError:
            if value < 0:
                print("value must be >= 0")
       

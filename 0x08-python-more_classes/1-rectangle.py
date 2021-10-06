#!/usr/bin/python3
"""Defines an empty class of a rectangle
"""


class Rectangle:
    """Rectangle class"""
    
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    """retrieves width"""
    def width(self): 
        return self.__width

    @width.setter
    """sets width"""
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        else:
            self.__width = value

    @property
    """retrieves height"""
     def height(self):
         return self.__height

    @height.setter
    """sets height"""
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        else:
            self.__height = value

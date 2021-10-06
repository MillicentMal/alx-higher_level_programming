#!/usr/bin/python3
"""Defines a class of a rectangle"""


class Rectangle:
    """Rectangle class"""
    
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def __str__(self):
        """return string representation of rectangle"""
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle
        for i in range(self.__height - 1):
            rectangle += "#" * self.__width + "\n"
        rectangle += "#" * self.__width
        
        return rectangle
                                                                                        
    @property
    def width(self): 
        return self.__width

    @width.setter
    def width(self, value):
        """Gets the width"""
        self.__width = value

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        

    @property
    def height(self):
         return self.__height

    @height.setter
    def height(self, value):
        """Gets the height"""
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("valu must be >= 0")
        
    

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2*self.__width + 2 * self.__height




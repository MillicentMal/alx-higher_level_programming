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
    
    def __repr__(self):
        """
            returns string representation of rectangle
            representation able to be recreated into a new instance
            using eval
        """
        rectangle = ''
        if self.__width is 0 or self.__height is 0:
            return rectangle
        rectangle = 'Rectangle({}, {})'.format(self.__width, self.__height)
        return rectangle
     
    def __del__(self):
        """
            prints Bye rectangle... when an instance is
            deleted
        """
        print('Bye rectangle...')
        

  

#!/usr/bin/python3
"""This is a square class that defines a square
"""


class Square:
    """This is a square class that defines a square
    """
    def __init__(self, size):
        """Defines a private attribute size
    """

        self.__size = size
        size = Square(size)

#!/usr/bin/python3
"""This is a square class that defines a square
"""


class Square:
    """This is a square class that defines a square
    """
    def __init__(self, size=0):
        """Optional instantiation
  """
       

        self.__size = size
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        print("Setting size")
        self.__size = size
        size = Square(value)

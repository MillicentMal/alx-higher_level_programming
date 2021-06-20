

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
    
    @property
    def size(self):
        """Getter method
    """
        print("Retrieving square size")
        return self.__size
   
    @size.setter
    def size(self, value):
        """Setter method
        """
    print("Setting size")
    self.__size = size

#!/usr/bin/python3
""" 
contains the Base class and its methods
"""

class Base:
    """ 
    base class
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """ 
        initialising objects 
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

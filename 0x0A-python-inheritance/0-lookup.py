#!/usr/bin/python3
"""
    Returns list of object attributes and methods
    """
def lookup(obj):
    """returns a list of all attributes and methods of a class
    """
    return dir(obj)

print(lookup(int))

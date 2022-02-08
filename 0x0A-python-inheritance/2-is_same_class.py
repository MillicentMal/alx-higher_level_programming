#!/usr/bin/python3
"""
    checks if object is an instance of a specified class
    """
    
def is_same_class(obj, a_class):
    """
    Returns:
        True or False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False 
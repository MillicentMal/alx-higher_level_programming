#!/usr/bin/python3
"""Adds a and b if only a and b are integers or floats. 
return sum of a and b """


def add_integer(a, b=98):
    """Adds integers a and b and returns their sum"""
    if not isinstance(b, float) and not isinstance(b, int) or not isinstance(a, float) and not isinstance(a, int):
        raise TypeError("a must be an integer or b must be an integer")
    else:
        return int(a) + int(b)

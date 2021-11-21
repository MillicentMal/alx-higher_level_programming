#!/usr/bin/python3
"""Adds a and b if only a and b are integers or floats
return sum of a and b """


def add_integer(a, b=98):
    """Add a to b and return the result.
    All arguments that are floats will be typecasted to ints
    Raises:
        TypeError: when a or b are neither integers nor floats.
    """

    if ((not isinstance(b, float) and not isinstance(b, int))):
        raise TypeError("b must be an integer")
    if ((not isinstance(a, float) and not isinstance(a, int))):
        raise TypeError("a must be an integer")
    else:
        return int(a) + int(b)

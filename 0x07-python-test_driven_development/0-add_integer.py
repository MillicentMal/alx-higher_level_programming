#!/usr/bin/python3
"""Adds a and b if only a and b are integers or floats. 
return sum of a and b """


def add_integer(a, b=98):
    """Adds integers a and b and returns their sum"""
    if not isinstance(b, float)  and  not isinstance(b, int) or not isinstance(a, float)  and not isinstance(a, int) :
        raise TypeError("a must be an integer or b must be an integer")
    else:
        return int(a) + int(b)


print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)

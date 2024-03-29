#!/usr/bin/python3
"""
Contains say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    returns the string 'My name is first_name + last_name'
    """

    if (not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if (not isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    else:
        print("My name is " + first_name + " " + last_name)

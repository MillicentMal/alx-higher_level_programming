#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    returns the string 'My name is first_name + last_name'
    """

    if isinstance(first_name, str) and isinstance(last_name, str):
        print("My name is " + first_name + " " + last_name)
    else:
        raise TypeError("first_name must be a string or last_name must be a string")

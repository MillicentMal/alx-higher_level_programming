#!/usr/bin/python3
""" 100-my_int: class MyInt """


class MyInt(int):
    """
    Rebel integer
    """

    def __init__(self, value):
        self.value = value

    def __eq__(self, obj):
        return isinstance(obj, MyInt) and obj.value == self.value

    def __ne__(self, obj):
        return not self == obj

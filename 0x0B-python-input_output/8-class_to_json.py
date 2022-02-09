#!/usr/bin/python3
""" converting class to json """


def class_to_json(obj):
    """
        returns dict of class
    """
    return obj.__dict__

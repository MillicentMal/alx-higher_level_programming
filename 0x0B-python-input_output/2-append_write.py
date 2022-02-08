#!/usr/bin/python3
"""
    appending to file using with
"""


def append_write(filename="", text=""):
    """
    function that appends to a text file (UTF8) and prints it to stdout
    """

    with open(filename, mode='a', encoding='UTF-8') as textfile:
        return textfile.write(text)

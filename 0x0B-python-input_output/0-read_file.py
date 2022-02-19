#!/usr/bin/python3
"""
Reading file using with
"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout
    """

    with open(filename, encoding='UTF-8') as textfile:
        print(textfile.read(), end='')

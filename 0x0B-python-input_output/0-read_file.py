#!/usr/bin/python3
""" 
Reading file using with
"""

def read_file(filename=""):
    """ 
    function that reads a text file (UTF8) and prints it to stdout
    """
    
    with open(filename, 'r') as textfile:
        print(textfile.read())


read_file("my_file_0.txt")

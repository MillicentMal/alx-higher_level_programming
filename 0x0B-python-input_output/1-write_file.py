#!/usr/bin/python3
""" 
Reading file using with
"""

def write_file(filename="", text=""):
    """ 
    function that writes to a text file (UTF8) and prints it to stdout
    """
    
    with open(filename, mode='w', encoding='UTF-8') as textfile:
        textfile.write(text)

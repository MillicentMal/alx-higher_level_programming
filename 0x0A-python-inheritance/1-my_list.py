#!/usr/bin/python3
""" 
MyList class
"""


class MyList(list):
    """
    inherits from list object
    """
    def __init__(self):
        self.obj = list()
    
    def print_sorted(self):
        print(sorted(self))
    



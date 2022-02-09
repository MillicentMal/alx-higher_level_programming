#!/usr/bin/python3
""" 
read json file
"""

import json


def load_from_json_file(filename):
    """ 
    read json file
    """

    with open(filename, 'r') as json_file:
        return json.load(json_file)


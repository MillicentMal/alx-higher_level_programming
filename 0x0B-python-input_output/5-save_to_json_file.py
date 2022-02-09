#!/usr/bin/python3
""" 
write to json file
"""

import json


def save_to_json_file(my_obj, filename):
    """ 
    writing to json file
    """

    with open(filename, 'w') as json_file:
        return json_file.write(json.dumps(my_obj))
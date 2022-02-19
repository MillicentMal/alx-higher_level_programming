#!/usr/bin/python3
"""
Convert JSON to python
"""
import json


def from_json_string(my_str):
    """
    returns JSON object to python
    """
    return json.loads(my_str)

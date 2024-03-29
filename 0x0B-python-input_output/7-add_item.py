#!/usr/bin/python3
"""Adding objects to a list in json file
"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('8-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        data = []
    data.extend(sys.argv[1:])
    save_to_json_file(data, "add_item.json")

#!/usr/bin/python3
"""
adding new string after search string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    adding new string after search string
    """
    text = ''
    with open(filename) as read_file:
        for line in read_file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as write_file:
        write_file.write(text)


append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")

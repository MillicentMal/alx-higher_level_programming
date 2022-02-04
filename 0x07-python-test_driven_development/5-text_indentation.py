#!/usr/bin/python3


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    new_string = ''
    delimiters = ['.', '?', ':']
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        for i in text:
            new_string += i
            if i in delimiters:
                print(new_string)
                print()
                new_string.clear()
            print(new_string)

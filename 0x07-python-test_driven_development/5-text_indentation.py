#!/usr/bin/python3


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    new_string = []
    delimiters = ['.', '?', ':']
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        for i in text:
            new_string.append(i)
            if i in delimiters:
                print(''.join(new_string))
                print()
                print()
                new_string.clear()

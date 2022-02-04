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
        for i in range(len(text)):
            new_string.append(text[i])
            if text[i] in delimiters:
                print(new_string)
                print()
                new_string.clear()
            elif text[i - 1] in delimiters:
                print(new_string)
                new_string.clear()

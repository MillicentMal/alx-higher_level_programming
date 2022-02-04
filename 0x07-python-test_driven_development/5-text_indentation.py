#!/usr/bin/python3


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    start = 0
    end = 0
    delimiters = ['.', '?', ':']
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
    delimiters = ['.', '?', ':']
    new_string = text
    start = 0
    for i in range(len(text)):
        if text[i] in delimiters:
            print(text[start:i+1].lstrip('.:?').strip())
            print()
            print()
            start = i
            new_string = text[i:]
    print(new_string.lstrip(':.?'))
                
    

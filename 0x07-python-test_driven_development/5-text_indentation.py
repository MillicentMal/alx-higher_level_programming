#!/usr/bin/python3


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    start = 0
    delimiters = ['.', '?', ':']
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        for i in range(len(text)):
        if text[i] in delimiters:
            end = i
            print(text[start:end+1])
            print()
            print()
            start = i + 1
    print(text[end + 1:], end="")
                
    

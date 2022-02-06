#!/usr/bin/python3
"""
text Indentation
"""

from matplotlib.pyplot import text


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    stringList = []
    delimiters = ['.', '?', ':']
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        for string in text:
            if string in delimiters:
                stringList.append(string + '\n\n')
            else:
                stringList.append(string)
    
        stringList = ''.join(stringList)
    print(stringList)







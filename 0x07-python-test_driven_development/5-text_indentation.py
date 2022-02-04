#!/usr/bin/python3


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    
    new_string = [text[:]]
    print(new_string)
    start = 0
    delimiters = ['.', '?', ':']
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        for i in range(len(text)):
            if i in delimiters:
                s = text[start:i+1] + \n\n
                new_string.append(s)
                start = i + 1
            else:
                s = text[start:]
   for string in new_string:
    print(string)
                
    

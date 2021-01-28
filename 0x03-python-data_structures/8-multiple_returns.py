#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        faracter = "None"
    else:
        faracter = sentence[0:1]

    return length, faracter

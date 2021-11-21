#!/usr/bin/python3
"""Function to find the peak of a list of integers
"""


def find_peak(list_of_integers):
    """returns the peak in a list of integers
    """
    if len(list_of_integers) != 0:
        return max(list_of_integers)
    else:
        return None

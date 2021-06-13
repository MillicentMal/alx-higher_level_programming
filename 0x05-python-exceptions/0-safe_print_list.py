#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        my_list = []
        i = 0
        for element in range(x):
            if type(element) == int:
                return element
            i += 1
    except:
        if IndexError:
            pass
    finally:
        return i

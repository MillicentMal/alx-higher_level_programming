#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    my_list = []
    i = 0
    for element in range(x):
        try:    
            if type(element) == int:
                print("{:d}".format(my_list[element]), end="")
            i += 1
        except:
            if IndexError:
                break
    print("")
    return i

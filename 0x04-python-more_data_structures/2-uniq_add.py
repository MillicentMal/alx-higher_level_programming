#!/usr/bin/python3

# only sums up the unique characters of a list


def uniq_add(my_list=[]):
    uniq_list = list(set(my_list))
    result = 0
    for i in range(0, len(uniq_list)):
        result += uniq_list[i]
    return result

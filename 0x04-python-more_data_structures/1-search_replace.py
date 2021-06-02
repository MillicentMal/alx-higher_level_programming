#!/usr/bin/python3
def search_replace(my_list, search, replace):
    i = 0
    while i != len(my_list):
        if my_list[i] != search:
            new_list.append(my_List[i])
        else:
            new_list.append(replace)
    return new_list


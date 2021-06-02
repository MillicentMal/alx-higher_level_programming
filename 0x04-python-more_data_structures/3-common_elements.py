#!/usr/bin/python3
# Function that returns a set of all elements present in only one set


def common_elements(set_1, set_2):
    sorted_set = []
    od_set = []
    for i in set_1:
        sorted_set.append(i)
    for j in set_2:
        sorted_set.append(j)
    print(sorted_set)

    sorted_set.sort()
    print(sorted_set)

    k = len(sorted_set)
    while k >= 0:
        k -= 1
        if sorted_set[k] == sorted_set[k-1]:
            pass
            od_set.append(sorted_set[k])
        return set(od_set)

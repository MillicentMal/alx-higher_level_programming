#!/usr/bin/python3


def print_square(size):
    """
    prints a square of size using #
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, int)  and size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for j in range(size):
                 print("#",  end="")
            print()


print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")
#!/usr/bin/python3
"""
    Matrix division
    """


def matrix_divided(matrix, div):
    """[summary]

    Args:
        matrix (List): of integers and floats
        div (int / float): the number to divide matrix with

    Returns:
        new list of lists
    """
    list_length = []
    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        list_length.append(len(matrix[i]))
        for num in matrix[i]:
            if not isinstance(num, int) and not isinstance(num, float):
                raise TypeError(
                    "matrix must be a matrix (list of lists) \
                    of integers/floats")
            elif not isinstance(matrix[i], list):
                raise TypeError(
                    "matrix must be a matrix (list of lists) \
                    of integers/floats")
    if len(set(list_length)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    new_matrix = []
    for i in matrix:
        new_matrix.append(list(map(lambda x: round(x / div, 2), i)))
    return new_matrix

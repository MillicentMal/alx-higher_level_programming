#!/usr/bin/python3

def matrix_divided(matrix, div):
    try:
        return map(lambda x, y: round(x / y , 2), matrix, div)
    except:
        if div == 0:
            return ZeroDivisionError("division by zero")
        elif not isinstance(div, int) or not isinstance(div, float):
            return TypeError("div must be a number")
        else:
            for i in range(len(matrix)):
                if not isinstance(matrix[i], list):
                    return TypeError("matrix must be a matrix (list of lists) of integers/floats")
                elif len(matrix[i]) != len(matrix[i + 1]):
                    return TypeError("Each row of the matrix must have the same size")
                else:
                    for num in matrix[i]:
                        if not isinstance(num, int) or not isinstance(num, float):
                            return TypeError("matrix must be a matrix (list of lists) of integers/floats")

    


#!/usr/bin/python3
""" 
lazy multiplication
"""


import numpy as np
def lazy_matrix_mul(m_a, m_b):
    try:
        return np.dot(m_a, m_b)
    
    except:
            """[summary]

    Args:
        2 matrices m_a and m_b to multiply each other

    Returns:
        list of products
    """
    itb = iter(m_b)
    the_len_b = len(next(itb))
    ita = iter(m_a)
    the_len_a = len(next(ita))
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
#     it = iter(lists)
# the_len = len(next(it))
    elif not all(isinstance(item, list) for item in m_a):
        raise TypeError("m_a must be a list or m_b must be a list")
    elif not all(isinstance(item, list) for item in m_b):
        raise TypeError("m_a must be a list or m_b must be a list")
    elif not all(isinstance(i, int) or isinstance(i, float) for item in m_b for i in item):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")
    elif not all(isinstance(i, int) or isinstance(i, float) for item in m_a for i in item):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")
    elif len(m_a) < 1 or len(m_b) < 1:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    elif not all(len(i) == the_len_b for i in itb) or not all(len(j) == the_len_b for j in ita):
        raise ValueError("each row of m_a must be of the same size or each row of m_b must be of the same size")
 
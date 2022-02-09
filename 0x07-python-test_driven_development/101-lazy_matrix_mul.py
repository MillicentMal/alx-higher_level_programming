#!/usr/bin/python3
""" 
lazy multiplication
"""


import numpy as np
def lazy_matrix_mul(m_a, m_b):
    try:
        return np.dot(m_a, m_b)
    
    except ValueError:
        return "Failed to multiply"
 
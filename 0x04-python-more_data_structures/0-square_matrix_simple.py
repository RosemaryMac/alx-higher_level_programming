#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [list(join((lambda x: x * x), elm)) for elm in matrix]

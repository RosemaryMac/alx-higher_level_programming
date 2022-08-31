#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix = [
            [2, 3, 4],
            [5, 6, 7],
            ]

    for x in matrix:
        new_matrix = square_matrix_simple(x ** 2)
        print(f"new_matrix")
        print(f"matrix")

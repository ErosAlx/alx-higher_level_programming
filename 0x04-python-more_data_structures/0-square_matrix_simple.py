#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        transpose = []
        for element in row:
            element = element * element
            transpose.append(element)
        new_matrix.append(transpose)
    return new_matrix

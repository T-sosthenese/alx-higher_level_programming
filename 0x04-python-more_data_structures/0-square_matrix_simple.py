#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    columns = len(matrix[0])
    rows = len(matrix)
    newest_matrix = [[0 for k in range(columns)] for j in range(rows)]
    for j in range(rows):
        for i in range(columns):
            newest_matrix[i][j] = matrix[i][j] ** 2
    return newest_matrix

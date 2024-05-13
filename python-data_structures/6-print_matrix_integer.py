#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row_idx in range(len(matrix)):
        row_length = len(matrix[row_idx])
        for col_idx in range(row_length):
            if col_idx != row_length - 1:
                end_char = ' '
            else:
                end_char = ''
            print("{:d}".format(matrix[row_idx][col_idx]), end=end_char)
        print("")

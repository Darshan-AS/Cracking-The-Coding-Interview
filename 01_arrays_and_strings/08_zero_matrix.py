"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to 0.
"""

from itertools import product

import pytest


def zero_out_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """
    Time:   O(MN)
    Space:  O(1)
    where,  M = number of rows in matrix, N = number of columns in matrix
    """
    M, N = len(matrix), len(matrix[0])

    first_row_has_zero = any(matrix[0][j] == 0 for j in range(N))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(M))

    # Check for zeros in the rest of the matrix
    # Mark the corresponding first row or column
    for i, j in product(range(M), range(N)):
        if matrix[i][j] == 0:
            matrix[i][0] = matrix[0][j] = 0

    # Nullify columns based on values in first row
    for j in range(1, N):
        if matrix[0][j] == 0:
            nullify_col(M, j, matrix)

    # Nullify rows based on values in first column
    for i in range(1, M):
        if matrix[i][0] == 0:
            nullify_row(N, i, matrix)

    # Nullify first row
    if first_row_has_zero:
        nullify_row(N, 0, matrix)

    # Nullify first column
    if first_col_has_zero:
        nullify_col(M, 0, matrix)

    return matrix


def nullify_row(N: int, i: int, matrix: list[list[int]]):
    for j in range(N):
        matrix[i][j] = 0


def nullify_col(M: int, j: int, matrix: list[list[int]]):
    for i in range(M):
        matrix[i][j] = 0


@pytest.mark.parametrize(
    "matrix, zeroed_out_matrix",
    [
        (
            [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 24, 0],
            ],
        )
    ],
)
def test_zero_out_matrix(matrix: list, zeroed_out_matrix: list):
    assert zero_out_matrix(matrix) == zeroed_out_matrix

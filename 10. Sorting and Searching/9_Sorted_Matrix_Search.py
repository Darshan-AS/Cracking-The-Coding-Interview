"""
Sorted Matrix Search: Given an M x N matrix in which each row and each column is sorted in ascending order,
write a method to find an element.
"""
import pytest


def sorted_matrix_search(matrix, key):
    def sorted_matrix_search_helper(left, right):
        top_left, mid, bottom_right = left, None, right
        
        while top_left[0] <= bottom_right[0] and top_left[1] <= bottom_right[1]:
            
            mid = (top_left[0] + bottom_right[0]) // 2, (top_left[1] + bottom_right[1]) // 2
            
            if key < matrix[mid[0]][mid[1]]:
                bottom_right = mid[0] - 1, mid[1] - 1
            elif key > matrix[mid[0]][mid[1]]:
                top_left = mid[0] + 1, mid[1] + 1
            else:
                return mid
        
        if not mid:
            return
        
        if key > matrix[mid[0]][mid[1]]:
            return sorted_matrix_search_helper((left[0], mid[1] + 1), (mid[0], right[1])) or \
                   sorted_matrix_search_helper((mid[0] + 1, left[1]), (right[0], mid[1]))
        elif key < matrix[mid[0]][mid[1]]:
            return sorted_matrix_search_helper((left[0], mid[1]), (mid[0] - 1, right[1])) or \
                   sorted_matrix_search_helper((mid[0], left[1]), (right[0], mid[1] - 1))
    
    return sorted_matrix_search_helper((0, 0), (len(matrix) - 1, len(matrix[0]) - 1))


@pytest.mark.parametrize('matrix, key, index_expected', [
    ([[]], 1, None),
    ([[1]], 1, (0, 0)),
    ([[1, 2, 3, 4]], 3, (0, 2)),
    ([[1],
      [2],
      [3],
      [4]], 3, (2, 0)),
    ([[1, 2],
      [3, 4]], 2, (0, 1)),
    ([[1, 2, 3],
      [4, 5, 6]], 6, (1, 2)),
    ([[1, 2, 3, 4, 5, 6, 7, 8, 9],
      [5, 10, 15, 20, 25, 30, 35, 40, 45],
      [10, 20, 30, 40, 50, 60, 70, 80, 90],
      [13, 23, 33, 43, 53, 63, 73, 83, 93],
      [14, 24, 34, 44, 54, 64, 74, 84, 94],
      [15, 25, 35, 45, 55, 65, 75, 85, 95],
      [16, 26, 36, 46, 56, 66, 77, 88, 99]], 10, (1, 1)),
    ([[1, 2, 3, 4, 5, 6, 7, 8, 9],
      [5, 10, 15, 20, 25, 30, 35, 40, 45],
      [10, 20, 30, 40, 50, 60, 70, 80, 90],
      [13, 23, 33, 43, 53, 63, 73, 83, 93],
      [14, 24, 34, 44, 54, 64, 74, 84, 94],
      [15, 25, 35, 45, 55, 65, 75, 85, 95],
      [16, 26, 36, 46, 56, 66, 77, 88, 99]], 74, (4, 6)),
    ([[1, 2, 3, 4, 5, 6, 7, 8, 9],
      [5, 10, 15, 20, 25, 30, 35, 40, 45],
      [10, 20, 30, 40, 50, 60, 70, 80, 90],
      [13, 23, 33, 43, 53, 63, 73, 83, 93],
      [14, 24, 34, 44, 54, 64, 74, 84, 94],
      [15, 25, 35, 45, 55, 65, 75, 85, 95],
      [16, 26, 36, 46, 56, 66, 77, 88, 99]], 99, (6, 8)),
    ([[1, 2, 3, 4, 5, 6, 7, 8, 9],
      [5, 10, 15, 20, 25, 30, 35, 40, 45],
      [10, 20, 30, 40, 50, 60, 70, 80, 90],
      [13, 23, 33, 43, 53, 63, 73, 83, 93],
      [14, 24, 34, 44, 54, 64, 74, 84, 94],
      [15, 25, 35, 45, 55, 65, 75, 85, 95],
      [16, 26, 36, 46, 56, 66, 77, 88, 99]], 13, (3, 0)),
    ([[1, 2, 3, 4, 5, 6, 7, 8, 9],
      [5, 10, 15, 20, 25, 30, 35, 40, 45],
      [10, 20, 30, 40, 50, 60, 70, 80, 90],
      [13, 23, 33, 43, 53, 63, 73, 83, 93],
      [14, 24, 34, 44, 54, 64, 74, 84, 94],
      [15, 25, 35, 45, 55, 65, 75, 85, 95],
      [16, 26, 36, 46, 56, 66, 77, 88, 99]], 56, (6, 4)),
])
def test_sorted_matrix_search(matrix, key, index_expected):
    assert sorted_matrix_search(matrix, key) == index_expected


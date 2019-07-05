"""
Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B.
Write a method to merge B into A in sorted order.
"""
import pytest


def sort_merge(sorted_a, sorted_b):
    # Index of last element in array b
    b_index = len(sorted_b) - 1
    # Index of last element in array a
    a_index = len(sorted_a) - len(sorted_b) - 1
    # End of merged array
    merged_index = len(sorted_a) - 1
    
    # Merge a and b, starting from the last element in each
    while b_index >= 0:
        if a_index >= 0 and sorted_a[a_index] > sorted_b[b_index]:
            sorted_a[merged_index] = sorted_a[a_index]
            a_index -= 1
        else:
            sorted_a[merged_index] = sorted_b[b_index]
            b_index -= 1
        merged_index -= 1
    
    return sorted_a


@pytest.mark.parametrize('sorted_a, sorted_b, sorted_merged_expected', [
    ([],
     [],
     []),
    ([1, None],
     [2],
     [1, 2]),
    ([1, 3, None, None],
     [2, 4],
     [1, 2, 3, 4]),
    ([33, 44, 55, 66, 88, 99, None, None, None],
     [11, 22, 77],
     [11, 22, 33, 44, 55, 66, 77, 88, 99])
])
def test_sorted_merge(sorted_a, sorted_b, sorted_merged_expected):
    assert sort_merge(sorted_a, sorted_b) == sorted_merged_expected

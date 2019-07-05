"""
Sparse Search: Given a sorted array of strings that is interspersed with empty strings,
write a method to find the location of a given string.

EXAMPLE
Input:  ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', ''], ball
Output: 4
"""
import pytest


def sparse_search(array, key):
    low, high = 0, len(array) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if array[mid] == '':
            left, right = mid - 1, mid + 1
            while low <= left and right <= high:
                if array[left]:
                    mid = left
                    break
                elif array[right]:
                    mid = right
                    break
                left, right = left - 1, right + 1
        
        if key < array[mid]:
            high = mid - 1
        elif key > array[mid]:
            low = mid + 1
        else:
            return mid


@pytest.mark.parametrize('array, key, index_expected', [
    (['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', ''],
     'ball', 4),
    (['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', ''],
     'at', 0),
    (['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', ''],
     'dad', 10),
])
def test_sparse_search(array, key, index_expected):
    assert sparse_search(array, key) == index_expected

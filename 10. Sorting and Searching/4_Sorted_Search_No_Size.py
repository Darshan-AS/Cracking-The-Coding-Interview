"""
Sorted Search, No Size: You are given an array like data structure Listy which lacks a size method.
It does, however, have an elementAt(i) method that returns the element at index i in 0(1) time.
If i is beyond the bounds of the data structure, it returns -1.
(For this reason, the data structure only supports positive integers.)
Given a Li sty which contains sorted, positive integers, find the index at which an element x occurs.
If x occurs multiple times, you may return any index.
"""
import pytest


class Listy:
    
    def __init__(self, array):
        self.array = sorted(array)
    
    # Indexing as substitute for elementAt method
    def __getitem__(self, index):
        return self.array[index] if index < len(self.array) else -1
    
    def __repr__(self):
        return repr(self.array)


def search_listy(listy, element):
    n = 1
    while listy[n] != -1 and listy[n] < element:
        n *= 2
    
    def binary_search_listy(low, high):
        while low <= high:
            mid = (low + high) // 2
            if element < listy[mid] or listy[mid] == -1:
                high = mid - 1
            elif element > listy[mid]:
                low = mid + 1
            else:
                return mid
    
    return binary_search_listy(n // 2, n)


@pytest.mark.parametrize('listy, element, index_expected', [
    (Listy([]), 1, None),
    (Listy([7]), 7, 0),
    (Listy([1, 2]), 1, 0),
    (Listy([1, 2, 3]), 3, 2),
    (Listy([1, 2, 3, 4]), 3, 2),
    (Listy([1, 2, 3, 4]), 7, None),
    (Listy([3, 12, 23, 23, 33, 40, 44, 45, 87, 98, 290, 583]), 3, 0),
    (Listy([3, 12, 23, 23, 33, 40, 44, 45, 87, 98, 290, 583]), 98, 9),
])
def test_search_listy(listy, element, index_expected):
    assert search_listy(listy, element) == index_expected

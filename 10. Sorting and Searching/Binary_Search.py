import pytest


def binary_search(array, key):
    low, high = 0, len(array) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if key < array[mid]:
            high = mid - 1
        elif key > array[mid]:
            low = mid + 1
        else:
            return mid


@pytest.mark.parametrize('array, key, index_expected', [
    ([], 1, None),
    ([7], 7, 0),
    ([1, 2], 1, 0),
    ([1, 2, 3], 3, 2),
    ([1, 2, 3, 4], 3, 2),
    ([1, 2, 3, 4], 7, None),
    ([3, 12, 23, 23, 33, 40, 44, 45, 87, 98, 290, 583], 3, 0),
    ([-9, -5, -3, -1, 0, 2, 3, 5, 7], -3, 2)
])
def test_binary_search(array, key, index_expected):
    assert binary_search(array, key) == index_expected

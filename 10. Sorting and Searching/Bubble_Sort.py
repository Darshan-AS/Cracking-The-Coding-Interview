import pytest


def bubble_sort(array):
    array = array.copy()
    n = len(array)
    
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                
    return array


@pytest.mark.parametrize('array, sorted_array_expected', [
    ([],
     []),
    ([7],
     [7]),
    ([2, 1],
     [1, 2]),
    ([2, 1, 3],
     [1, 2, 3]),
    ([3, 4, 1, 2], [1, 2, 3, 4]),
    ([44, 23, 87, 12, 3, 98, 40, 23, 45, 583, 290, 33],
     [3, 12, 23, 23, 33, 40, 44, 45, 87, 98, 290, 583]),
    ([2, 5, -1, 3, -5, -3, 7, 0, -9],
     [-9, -5, -3, -1, 0, 2, 3, 5, 7])
])
def test_bubble_sort(array, sorted_array_expected):
    assert bubble_sort(array) == sorted_array_expected

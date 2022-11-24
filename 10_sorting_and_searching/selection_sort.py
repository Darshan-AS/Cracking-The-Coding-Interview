import pytest


def selection_sort(array):
    array = array.copy()
    n = len(array)
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            min_index = min_index if array[min_index] < array[j] else j
        array[i], array[min_index] = array[min_index], array[i]
    
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
def test_selection_sort(array, sorted_array_expected):
    assert selection_sort(array) == sorted_array_expected

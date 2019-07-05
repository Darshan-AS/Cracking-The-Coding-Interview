import pytest


def merge_sort(array):
    array = array.copy()
    n = len(array)
    
    if n <= 1:
        return array
    
    mid = n // 2
    left_sorted_half = merge_sort(array[:mid])
    right_sorted_half = merge_sort(array[mid:])
    
    i, j, k = 0, 0, 0
    while i < len(left_sorted_half) and j < len(right_sorted_half):
        
        if left_sorted_half[i] < right_sorted_half[j]:
            array[k] = left_sorted_half[i]
            i += 1
        else:
            array[k] = right_sorted_half[j]
            j += 1
            
        k += 1
    
    while i < len(left_sorted_half):
        array[k] = left_sorted_half[i]
        i += 1
        k += 1
        
    while j < len(right_sorted_half):
        array[k] = right_sorted_half[j]
        j += 1
        k += 1
    
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
def test_merge_sort(array, sorted_array_expected):
    assert merge_sort(array) == sorted_array_expected

import pytest


def quick_sort(array):
    array = array.copy()
    
    def quick_sort_helper(start, end):
        if start >= end:
            return
        
        pivot = array[start]
        low, high = start + 1, end
        while True:
            while low <= high and array[low] <= pivot:
                low += 1
            
            while low <= high and array[high] >= pivot:
                high -= 1
            
            if low < high:
                array[low], array[high] = array[high], array[low]
            else:
                break
        
        array[start], array[high] = array[high], array[start]
        
        quick_sort_helper(start, high - 1)
        quick_sort_helper(high + 1, end)
    
    quick_sort_helper(0, len(array) - 1)
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
    ([3, 4, 1, 2],
     [1, 2, 3, 4]),
    ([44, 23, 87, 12, 3, 98, 40, 23, 45, 583, 290, 33],
     [3, 12, 23, 23, 33, 40, 44, 45, 87, 98, 290, 583]),
    ([2, 5, -1, 3, -5, -3, 7, 0, -9],
     [-9, -5, -3, -1, 0, 2, 3, 5, 7])
])
def test_quick_sort(array, sorted_array_expected):
    assert quick_sort(array) == sorted_array_expected

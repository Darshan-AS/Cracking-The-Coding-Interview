"""
Search in Rotated Array: Given a sorted array of n integers that has been rotated an unknown number of times,
write code to find an element in the array. You may assume that the array was originally sorted in increasing order.

EXAMPLE
Input:  find 5 in [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
Output: 8 (the index of 5 in the array)
"""
import pytest


def search_in_rotated_array(rotated_array, element):
    def search_in_rotated_array_helper(left, right):
        if left > right:
            return
        
        mid = (left + right) // 2
        
        if element == rotated_array[mid]:
            return mid
        
        left_element, middle_element, right_element = rotated_array[left], rotated_array[mid], rotated_array[right]
        
        # If can't figure out which side is ordered, search both
        if left_element == middle_element == right_element:
            return search_in_rotated_array_helper(left, mid - 1) or search_in_rotated_array_helper(mid + 1, right)
        # Left side is ordered
        elif left_element <= middle_element:
            if left_element <= element < middle_element:
                return search_in_rotated_array_helper(left, mid - 1)
            else:
                return search_in_rotated_array_helper(mid + 1, right)
        # Right side is ordered
        elif middle_element <= right_element:
            if middle_element < element <= right_element:
                return search_in_rotated_array_helper(mid + 1, right)
            else:
                return search_in_rotated_array_helper(left, mid - 1)
    
    return search_in_rotated_array_helper(0, len(rotated_array) - 1)


@pytest.mark.parametrize('rotated_array, element, index_expected', [
    ([55, 60, 65, 70, 75, 80, 85, 90, 95, 15, 20, 25, 30, 35, 40, 45], 55, 0),
    ([55, 60, 65, 70, 75, 80, 85, 90, 95, 15, 20, 25, 30, 35, 40, 45], 60, 1),
    ([55, 60, 65, 70, 75, 80, 85, 90, 95, 15, 20, 25, 30, 35, 40, 45], 95, 8),
    ([55, 60, 65, 70, 75, 80, 85, 90, 95, 15, 20, 25, 30, 35, 40, 45], 30, 12),
    ([55, 60, 65, 70, 75, 80, 85, 90, 95, 15, 20, 25, 30, 35, 40, 45], 45, 15),
    ([10, 15, 20, 0, 5], 5, 4),
    ([50, 5, 20, 30, 40], 5, 1),
    ([2, 2, 2, 3, 4, 2], 3, 3),
    ([2, 2, 2, 3, 4, 2], 4, 4),
    ([2, 2, 2, 3, 4, 2], 2, 2)
])
def test_search_in_rotated_array(rotated_array, element, index_expected):
    assert search_in_rotated_array(rotated_array, element) == index_expected

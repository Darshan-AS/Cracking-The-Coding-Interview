"""
Peaks and Valleys: In an array of integers, a "peak" is an element which is greater than or equal to
the adjacent integers and a "valley" is an element which is less than or equal to the adjacent integers.
For example, in the array [5, 8, 6, 2, 3, 4, 6], {8, 6} are peaks and {5, 2} are valleys. Given an array
of integers, sort the array into an alternating sequence of peaks and valleys.
EXAMPLE
Input   : [5, 3, 1, 2, 3]
Output  : [5, 1, 3, 2, 3]
"""
import pytest


def peaks_and_valleys(array):
    for i in range(1, len(array) - 1, 2):
        if not array[i - 1] < array[i] > array[i + 1]:
            if array[i - 1] > array[i + 1]:
                array[i - 1], array[i] = array[i], array[i - 1]
            else:
                array[i + 1], array[i] = array[i], array[i + 1]
    return array


@pytest.mark.parametrize('array, sorted_array', [
    ([], []),
    ([1], [1]),
    ([1, 2], [1, 2]),
    ([1, 2, 3], [1, 3, 2]),
    ([5, 3, 1, 2, 3], [3, 5, 1, 3, 2]),
    ([12, 6, 3, 1, 0, 14, 13, 20, 22, 10], [6, 12, 1, 3, 0, 14, 13, 22, 20, 10]),
    ([34, 55, 60, 65, 70, 75, 85, 10, 5, 16], [34, 60, 55, 70, 65, 85, 10, 75, 5, 16])
])
def test_peaks_and_valleys(array, sorted_array):
    assert peaks_and_valleys(array) == sorted_array

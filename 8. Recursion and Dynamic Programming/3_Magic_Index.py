"""
Magic Index: A magic index in an array A [0 ••• n - 1] is defined to be an index such that A[i] = i.
Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.
FOLLOW UP:
What if the values are not distinct?
"""
import pytest


def magic_index_distinct(arr):
    def magic_index_helper(left, right):
        # Almost like BinarySearch
        if left > right:
            return
        mid = (left + right) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            return magic_index_helper(mid + 1, right)
        elif arr[mid] > mid:
            return magic_index_helper(left, mid - 1)

    return magic_index_helper(0, len(arr) - 1)


def magic_index(arr):
    def magic_index_helper(left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        if arr[mid] == mid:
            return mid

        # Search left
        left_index = magic_index_helper(left, min(mid - 1, arr[mid]))
        if left_index:
            return left_index

        # Search Right
        right_index = magic_index_helper(max(mid + 1, arr[mid]), right)
        if right_index:
            return right_index

    return magic_index_helper(0, len(arr) - 1)


@pytest.mark.parametrize('distinct_arr, magic_index_expected', [
    ([0], 0),
    ([4], None),
    ([3, 4, 5], None),
    ([-1, 0, 2], 2),
    ([-2, -1, 0, 2], None),
    ([-20, 0, 1, 2, 3, 4, 5, 6, 20], None),
    ([-20, 0, 1, 2, 3, 4, 5, 7, 20], 7),
    ([-20, 1, 2, 3, 4, 5, 6, 20], 3),
])
def test_magic_index_distinct(distinct_arr, magic_index_expected):
    assert magic_index_distinct(distinct_arr) == magic_index_expected


@pytest.mark.parametrize('arr, magic_index_expected', [
    ([3, 4, 5], None),
    ([-2, -1, 0, 2], None),
    ([-20, 0, 1, 2, 3, 4, 5, 6, 20], None),
    ([-20, 0, 1, 2, 3, 4, 5, 7, 20], 7),
    ([-20, 1, 2, 3, 4, 5, 6, 20], 3),
    ([-20, 5, 5, 5, 5, 5, 6, 20], 6)

])
def test_magic_index(arr, magic_index_expected):
    assert magic_index(arr) == magic_index_expected

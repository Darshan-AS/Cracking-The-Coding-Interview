import pytest


def linear_search(array, key):
    for i in range(len(array)):
        if array[i] == key:
            return i
    return None


@pytest.mark.parametrize('array, key, index_expected', [
    ([], 1, None),
    ([7], 7, 0),
    ([2, 1], 1, 1),
    ([2, 1, 3], 3, 2),
    ([3, 4, 1, 2], 3, 0),
    ([3, 4, 1, 2], 7, None),
    ([44, 23, 87, 12, 3, 98, 40, 23, 45, 583, 290, 33], 3, 4),
    ([2, 5, -1, 3, -5, -3, 7, 0, -9], -3, 5)
])
def test_linear_search(array, key, index_expected):
    assert linear_search(array, key) == index_expected

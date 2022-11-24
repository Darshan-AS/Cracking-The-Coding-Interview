"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
"""

import pytest

"""
Time:   O(N)
Space:  O(N)
where,  N = length of s1 = length of s2
"""


def check_permutation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    # Increment count for characters in s1
    count = {}
    for i in s1:
        if i not in count.keys():
            count[i] = 0
        count[i] += 1

    # Decrement count for characters in s2
    for j in s2:
        if j not in count.keys() or count[j] == 0:
            return False
        count[j] -= 1

    return True


@pytest.mark.parametrize('s1, s2, are_permutation', [
    ('abcd', 'bacd', True),
    ('3563476', '7334566', True),
    ('wef34f', 'wffe34', True),
    ('abcd', 'd2cba', False),
    ('2354', '1234', False),
    ('dcw4f', 'dcw5f', False),
    ('God   ', 'dog', False),
    ('abc', 'ab', False),
    ('sunil', 'unii', False)
])
def test_check_permutation(s1: str, s2: str, are_permutation: bool):
    assert check_permutation(s1, s2) == are_permutation

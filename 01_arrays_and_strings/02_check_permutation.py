"""
Check Permutation: Given two strings, write a method to decide
if one is a permutation of the other.
"""

from collections import Counter

import pytest


def check_permutation(s1: str, s2: str) -> bool:
    """
    Time:   O(N)
    Space:  O(N)
    where,  N = length of s1 = length of s2"""
    return len(s1) == len(s2) and Counter(s1) == Counter(s2)


@pytest.mark.parametrize(
    "s1, s2, are_permutation",
    [
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("God   ", "dog", False),
        ("abc", "ab", False),
        ("sunil", "unii", False),
    ],
)
def test_check_permutation(s1: str, s2: str, are_permutation: bool):
    assert check_permutation(s1, s2) == are_permutation

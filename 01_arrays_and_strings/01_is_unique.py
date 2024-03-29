"""
Is Unique: Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""

import pytest


def is_unique(s: str) -> bool:
    """
    Time:   O(N)
    Space:  O(N)
    where,  N = length of s
    """
    return len(set(s)) == len(s)


def is_unique_ascii(s: str) -> bool:
    """
    Time:   O(N)
    Space:  O(1)
    where,  N = length of s

    Assuming character set is ASCII (128 characters)
    """
    if len(s) > 128:
        return False

    char_set = [False] * 128
    for ch in s:
        if char_set[ord(ch)]:
            return False
        char_set[ord(ch)] = True
    return True


@pytest.mark.parametrize(
    "s, is_unique_expected",
    [
        ("Don", True),
        ("Ghost", True),
        ("Batman", False),
        ("L", True),
        ("", True),
        ("yfdtyrsgu", False),
    ],
)
def test_is_unique(s: str, is_unique_expected: str):
    assert is_unique(s) == is_unique_expected
    assert is_unique_ascii(s) == is_unique_expected

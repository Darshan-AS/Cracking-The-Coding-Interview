"""
String Rotation: Assume you have a method is_substring,
which checks if one word is a substring of another.
Given two strings, s1 and s2, write code to check
if s2 is a rotation of s1 using only one call to is_substring
(e.g., "waterbottle" is a rotation of "erbottlewat").
"""
import pytest


def is_rotation(s1: str, s2: str) -> bool:
    """
    Time:   O(N)
    Space:  O(1)
    where,  N = length of s1 or s2
    """
    return len(s1) == len(s2) and is_substring(s2, s1 + s1)


def is_substring(s1: str, s2: str) -> bool:
    """Checks if s1 is substring of s2"""
    return s1 in s2


@pytest.mark.parametrize(
    "s1, s2, is_substring_expected",
    [
        ("waterbottle", "erbottlewat", True),
        ("foo", "bar", False),
        ("foo", "foofoo", False),
    ],
)
def test_is_rotation(s1: str, s2: str, is_substring_expected: bool):
    assert is_rotation(s1, s2) == is_substring_expected

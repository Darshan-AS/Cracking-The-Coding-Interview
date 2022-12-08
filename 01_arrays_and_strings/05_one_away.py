"""
One Away: There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit (or zero edits) away.

EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""

import pytest


def is_one_away(s1: str, s2: str) -> bool:
    """
    Time:   O(N)
    Space:  O(1)
    where,  N = length of shorter string
    """
    n1, n2 = len(s1), len(s2)
    if abs(n1 - n2) > 1:
        return False

    short_s, long_s = (s1, s2) if n1 < n2 else (s2, s1)
    i, j, prev_mismatch_found = 0, 0, False

    while i < n1 and j < n2:
        curr_mismatch = short_s[i] != long_s[j]

        if prev_mismatch_found and curr_mismatch:
            return False

        prev_mismatch_found = prev_mismatch_found or curr_mismatch

        # If insert / replace increment both pointers
        # if remove increment only shorter pointer
        i, j = (i, j + 1) if n1 != n2 and curr_mismatch else (i + 1, j + 1)

    return True


@pytest.mark.parametrize(
    "s1, s2, is_one_away_expected",
    [
        ("pale", "ple", True),
        ("pales", "pale", True),
        ("pale", "bale", True),
        ("pale", "bake", False),
    ],
)
def test_is_one_away(s1: str, s2: str, is_one_away_expected: bool):
    assert is_one_away(s1, s2) == is_one_away_expected

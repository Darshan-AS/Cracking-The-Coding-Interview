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

"""
Time:   O(N)
Space:  O(1)
where,  N = length of shorter string
"""


def is_one_away(s1: str, s2: str) -> bool:
    if abs(len(s1) - len(s2)) > 1:
        return False

    short_s, long_s = (s1, s2) if len(s1) < len(s2) else (s2, s1)
    i, j, mismatch_found = 0, 0, False
    while i < len(short_s) and j < len(long_s):
        if short_s[i] != long_s[j]:
            # If there was already a mismatch return False else set mismatch
            if mismatch_found:
                return False
            else:
                mismatch_found = True

            # If insert / replace increment both pointers; if remove increment only shorter pointer
            i, j = (i + 1, j + 1) if len(short_s) == len(long_s) else (i, j + 1)
        else:
            i, j = i + 1, j + 1
    return True


@pytest.mark.parametrize('s1, s2, is_one_away_expected', [
    ('pale', 'ple', True),
    ('pales', 'pale', True),
    ('pale', 'bale', True),
    ('pale', 'bake', False)
])
def test_is_one_away(s1: str, s2: str, is_one_away_expected: bool):
    assert is_one_away(s1, s2) == is_one_away_expected

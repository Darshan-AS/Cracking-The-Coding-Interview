"""
String Compression: Implement a method to perform basic string compression
using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3.
If the "compressed" string would not become smaller than the original string,
your method should return the original string.
You can assume the string has only uppercase and lowercase letters (a - z).
"""

from itertools import groupby

import pytest


def compress(s: str) -> str:
    """
    Time:   O(N)
    Space:  O(N)
    where,  N = length of s
    """
    ilen = lambda iterable: sum(1 for _ in iterable)
    compressed_s = (ch + str(ilen(group)) for ch, group in groupby(s))
    return min(s, "".join(compressed_s), key=len)


def compress_2(s: str) -> str:
    """
    Time:   O(N)
    Space:  O(N)
    where,  N = length of s
    """
    if not s:
        return s

    compressed_s: list[str] = []
    current, count = s[0], 0
    for c in s:
        # If character is different than current, then append to compressed_s
        if c != current:
            compressed_s.extend((current, str(count)))
            current, count = c, 0
        count += 1
    compressed_s.extend((current, str(count)))
    return min(s, "".join(compressed_s), key=len)


@pytest.mark.parametrize(
    "s, compressed_s", [("aabcccccaaa", "a2b1c5a3"), ("abcdef", "abcdef"), ("", "")]
)
def test_compress(s: str, compressed_s: str):
    assert compress(s) == compressed_s
    assert compress_2(s) == compressed_s

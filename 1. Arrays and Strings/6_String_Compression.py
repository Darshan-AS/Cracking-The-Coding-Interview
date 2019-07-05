"""
String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2blc5a3.
If the "compressed" string would not become smaller than the original string,
your method should return the original string.
You can assume the string has only uppercase and lowercase letters (a - z).
"""
import pytest

"""
Time:   O(N)
Space:  O(N)
where,  N = length of s
"""


def compress(s: str) -> str:
    if len(s) <= 1:
        return s

    compressed_s, current, count = [], s[0], 0
    for c in s:
        # If character is different than current, then append to compressed_s
        if c != current:
            compressed_s.extend((current, str(count)))
            current, count = c, 0
        count += 1
    compressed_s.extend((current, str(count)))
    return ''.join(compressed_s) if len(compressed_s) < len(s) else s


@pytest.mark.parametrize('s, compressed_s', [
    ('aabcccccaaa', 'a2b1c5a3'),
    ('abcdef', 'abcdef'),
    ('', '')
])
def test_compress(s: str, compressed_s: str):
    assert compress(s) == compressed_s

"""
Flip Bit to Win: You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to
find the length of the longest sequence of 1s you could create.
EXAMPLE
Input: 1775 (or: 11011101111)
Output: 8
"""
import pytest


def flip_bit_to_win(n):
    if (n + 1) & n == 0:
        return len(bin(n)) - 2
    
    prev, curr, count = 0, 0, 1
    while n > 0:
        if n & 1:
            curr += 1
        elif n & 2:
            prev, curr = curr, 0
        else:
            prev, curr = 0, 0
        count = max(count, prev + 1 + curr)
        n >>= 1
    return count


@pytest.mark.parametrize('n, expected', [
    (0b0, 1),
    (0b1111111, 7),
    (0b11011101111, 8),
    (0b111100101, 5),
    (0b10101101011101101, 6)
])
def test_flip_bit_to_win(n, expected):
    assert flip_bit_to_win(n) == expected

"""
Insertion: You are given two 32-bit numbers, N and M, and two bit positions, i and
j. Write a method to insert M into N such that M starts at bit j and ends at bit i. You
can assume that the bits j through i have enough space to fit all of M. That is, if
M = 10011, you can assume that there are at least 5 bits between j and i. You would not, for
example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.
EXAMPLE
Input:  N = 10000000000, M = 10011, i = 2, j = 6
Output: N = 10001001100
"""
import pytest


def insertion(n, m, i, j):
    left = ~0 << (j + 1)
    right = (1 << i) - 1
    mask = left | right
    
    n_cleared = n & mask
    m_shifted = m << i
    return n_cleared | m_shifted


@pytest.mark.parametrize('n, m, i, j, expected', [
    (0b10000000000, 0b10011, 2, 6, 0b10001001100),
    (0b101101000100110101010, 0b1101011, 3, 9,  0b101101000101101011010)
])
def test_insertion(n, m, i, j, expected):
    assert insertion(n, m, i, j) == expected

"""
Pairwise Swap: Write a program to swap odd and even bits in an integer with as few instructions as
possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).
"""
import pytest


def pairwise_swap(n):
    EVEN = 0x5555555555555555
    ODD = 0xAAAAAAAAAAAAAAAA
    return ((n & ODD) >> 1) | ((n & EVEN) << 1)


@pytest.mark.parametrize('n, expected', [
    (0b101010, 0b010101),
    (0b1010010, 0b10100001)
])
def test_pairwise_swap(n, expected):
    assert pairwise_swap(n) == expected

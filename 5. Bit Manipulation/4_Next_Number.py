"""
Next Number: Given a positive integer, print the next smallest and the next largest number that
have the same number of 1 bits in their binary representation.
"""
import pytest


def next_big(n):
    if n == 0:
        return
    
    c, c0, c1 = n, 0, 0
    
    while c & 1 == 0:
        c0 += 1
        c >>= 1
    
    while c & 1 == 1:
        c1 += 1
        c >>= 1
    
    p = c0 + c1
    n |= (1 << p)
    n &= ~((1 << p) - 1)
    n |= (1 << (c1 - 1)) - 1
    return n


def next_small(n):
    if n == 0:
        return
    
    c, c1, c0 = n, 0, 0
    
    while c & 1 == 1:
        c1 += 1
        c >>= 1
    
    while c & 1 == 0:
        c0 += 1
        c >>= 1
    
    p = c1 + c0
    n &= ~(1 << p)
    n &= ~((1 << p) - 1)
    n |= ((1 << (c1 + 1)) - 1) << c0 - 1
    return n


def next_number(n):
    return next_big(n), next_small(n)


@pytest.mark.parametrize('n, expected', [
    (0b101011, (0b101101, 0b100111)),
    (0b11011001111100, (0b11011010001111, 0b11011001111010))
])
def test_next_number(n, expected):
    assert next_number(n) == expected

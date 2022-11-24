"""
Conversion: Write a function to determine the number of bits you would need to flip to convert
integer A to integer B.
EXAMPLE
Input: 29 (or: 11101), 15 (or: 01111)
Output: 2
"""
import pytest


def conversion(n1, n2):
    n = n1 ^ n2
    
    count = 0
    while n != 0:
        if n & 1:
            count += 1
        n >>= 1
    return count


@pytest.mark.parametrize('n1, n2, expected', [
    (0b11101, 0b01111, 2),
    (0b1111, 0b1111, 0),
    (0b10101, 0b11101, 1)
])
def test_conversion(n1, n2, expected):
    assert conversion(n1, n2) == expected

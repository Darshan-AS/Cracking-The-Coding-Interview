"""
Debugger: Explain what the following code does: ((n & (n - 1)) == 0)
"""
import pytest


def debugger(n):
    """Checks if n is power of 2 i.e Checks if n in binary has one occurrence of bit 1"""
    return (n & (n - 1)) == 0


@pytest.mark.parametrize('n, expected', [
    (2 ** 4, True),
    (2 ** 5 - 1, False),
    (0b000100000, True),
    (0b00100101, False)
])
def test_debugger(n, expected):
    assert debugger(n) == expected

"""
Binary to String: Given a real number between O and 1 (e.g., 0.72) that is passed in as a double, print
the binary representation. If the number cannot be represented accurately in binary with at most 32
characters, print "ERROR:'
"""
import pytest


def binary_to_string(num):
    if num >= 1 or num <= 0:
        return 'ERROR'
    
    s = ['0.']
    while num > 0:
        if len(s) >= 32:
            return 'ERROR'
        
        r = num * 2
        if r >= 1:
            s.append(1)
            num = r - 1
        else:
            s.append(0)
            num = r
    return ''.join([str(i) for i in s])


@pytest.mark.parametrize('num, expected', [
    (0.72, 'ERROR'),
    (0.40625, '0.01101'),
    (1.2, 'ERROR')
])
def test_binary_to_string(num, expected):
    assert binary_to_string(num) == expected

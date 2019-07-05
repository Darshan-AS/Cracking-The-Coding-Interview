"""
Recursive Multiply: Write a recursive function to multiply two positive integers without using the * operator.
You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations
"""
import pytest


def recursive_multiply(a, b):
    smaller, larger = (a, b) if a < b else (b, a)
    
    def recursive_multiply_helper(small, large):
        if small == 0:
            return 0
        elif small == 1:
            return large
        
        # Divide by 2
        s = small >> 1
        half_prod = recursive_multiply_helper(s, large)
        
        # If even double the half_prod else double + large
        return half_prod + half_prod + large if small % 2 else half_prod + half_prod
    
    return recursive_multiply_helper(smaller, larger)


@pytest.mark.parametrize('a, b, product_expected', [
    (2, 2, 4),
    (1, 125, 125),
    (7, 11, 77),
    (10000000010, 21, 210000000210)
])
def test_recursive_multiply(a, b, product_expected):
    assert recursive_multiply(a, b) == product_expected

"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
"""

import pytest

"""
Time:   O(N)
Space:  O(1)
where,  N = length of s
"""


def is_palindrome_permutation(s: str) -> bool:
    # Use bit vector to indicate if character was seen
    bit_vector = 0

    for c in s:
        if c == ' ':
            continue
        mask = 1 << ord(c)
        # Set bit if unset and vice-versa
        bit_vector = bit_vector | mask if bit_vector & mask == 0 else bit_vector & ~mask

    return bit_vector == 0 or bit_vector & (bit_vector - 1) == 0


@pytest.mark.parametrize('s, is_palindrome_permutation_expected', [
    ('taco cat', True),
    ('jhg', False)
])
def test__is_palindrome_permutation(s: str, is_palindrome_permutation_expected: bool):
    assert is_palindrome_permutation(s) == is_palindrome_permutation_expected

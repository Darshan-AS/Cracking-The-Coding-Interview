"""
Palindrome Permutation: Given a string, write a function to check
if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
"""

from functools import reduce

import pytest


def is_palindrome_permutation(s: str) -> bool:
    """
    Time:   O(N)
    Space:  O(K)
    where,  N = length of s, K = length of charset
    """

    def mark_bit(bit_vector: int, ch: str) -> int:
        mask = 1 << ord(ch)
        # Set bit if unset and vice-versa
        return bit_vector | mask if bit_vector & mask == 0 else bit_vector & ~mask

    # Use bit vector to indicate if character was seen
    chars = filter(lambda ch: not ch.isspace(), s)
    bit_vector = reduce(mark_bit, chars, 0)

    return bit_vector == 0 or bit_vector & (bit_vector - 1) == 0


@pytest.mark.parametrize(
    "s, is_palindrome_permutation_expected",
    [
        ("taco cat", True),
        ("jhg", False),
    ],
)
def test__is_palindrome_permutation(s: str, is_palindrome_permutation_expected: bool):
    assert is_palindrome_permutation(s) == is_palindrome_permutation_expected

"""
Permutations without Duplicates: Write a method to compute all permutations of a string of unique characters.
"""
import pytest


def permutations_without_duplicates(s):
    if not s:
        return {s}
    
    permutations = set()
    
    for i, char in enumerate(s):
        # Remove char i and find permutations of remaining chars
        for permutation in permutations_without_duplicates(s[:i] + s[i + 1:]):
            # Prepend char i to each permutation
            permutations.add(char + permutation)
    
    return permutations


@pytest.mark.parametrize('s, permutations_expected', [
    ('ABCD', {'ABCD', 'ABDC', 'ACBD', 'ACDB',
              'ADBC', 'ADCB', 'BACD', 'BADC',
              'BCAD', 'BCDA', 'BDAC', 'BDCA',
              'CABD', 'CADB', 'CBAD', 'CBDA',
              'CDAB', 'CDBA', 'DABC', 'DACB',
              'DBAC', 'DBCA', 'DCAB', 'DCBA'})
])
def test_permutations_without_duplicates(s, permutations_expected):
    assert permutations_without_duplicates(s) == permutations_expected

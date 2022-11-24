"""
Permutations with Duplicates: Write a method to compute all permutations of a string whose characters 
are not necessarily unique. The list of permutations should not have duplicates
"""
from collections import Counter

import pytest


def permutations_with_duplicates(s):
    def permutation_helper(s_counter):
        
        if not s_counter - Counter():
            return {''}
        
        permutations = set()
        # Try remaining letters for next char, and generate remaining permutations.
        for char in s_counter.keys():
            if not s_counter[char]:
                continue
                
            next_counter = s_counter.copy()
            next_counter[char] -= 1
            for permutation in permutation_helper(next_counter):
                permutations.add(char + permutation)
                
        return permutations
    
    return permutation_helper(Counter(s))


@pytest.mark.parametrize('s, permutations_expected', [
    ('aba', {'aab',
             'baa',
             'aba'}),
    ('abca', {'aabc', 'aacb', 'abac', 'abca',
              'acab', 'acba', 'baac', 'baca',
              'bcaa', 'caab', 'caba', 'cbaa'}),
    ('ABCD', {'ABCD', 'ABDC', 'ACBD', 'ACDB',
              'ADBC', 'ADCB', 'BACD', 'BADC',
              'BCAD', 'BCDA', 'BDAC', 'BDCA',
              'CABD', 'CADB', 'CBAD', 'CBDA',
              'CDAB', 'CDBA', 'DABC', 'DACB',
              'DBAC', 'DBCA', 'DCAB', 'DCBA'})
])
def test_permutations_with_duplicates(s, permutations_expected):
    assert permutations_with_duplicates(s) == permutations_expected

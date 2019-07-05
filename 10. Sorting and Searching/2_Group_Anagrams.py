"""
Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to each other.
"""
from collections import defaultdict

import pytest


def group_anagrams(anagrams):
    anagrams_map = defaultdict(list)
    
    # Group words by anagram
    for a in anagrams:
        anagrams_map[''.join(sorted(a))].append(a)
    
    # Convert dict to array
    grouped_anagrams = []
    for anagram_group in anagrams_map.values():
        grouped_anagrams.extend(anagram_group)
    
    return grouped_anagrams


@pytest.mark.parametrize('anagrams, grouped_anagrams_expected', [
    (['cat', 'bat', 'rat', 'arts', 'tab', 'tar', 'car', 'star'],
     ['cat', 'bat', 'tab', 'rat', 'tar', 'arts', 'star', 'car'])
])
def test_group_anagrams(anagrams, grouped_anagrams_expected):
    assert group_anagrams(anagrams) == grouped_anagrams_expected

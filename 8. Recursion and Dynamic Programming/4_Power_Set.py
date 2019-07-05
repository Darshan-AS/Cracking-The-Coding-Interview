"""
Power Set: Write a method to return all subsets of a set.
"""
import pytest


def power_set(input_set):
    ps = {frozenset()}
    for element in input_set:
        additions = set()
        for subset in ps:
            # Add element to every previously generated set
            additions.add(subset.union(element))
        ps = ps.union(additions)
    return ps


@pytest.mark.parametrize('input_set, power_set_expected', [
    # (set(), [
    #     set()
    # ]),
    # ({'a'}, [
    #     set(), {'a'}
    # ]),
    ({'a', 'b', 'c', 'd'}, [
        set(), {'a'}, {'b'}, {'c'}, {'d'},
        {'a', 'b'}, {'a', 'c'}, {'a', 'd'}, {'b', 'c'}, {'b', 'd'}, {'c', 'd'},
        {'a', 'b', 'c'}, {'a', 'b', 'd'}, {'a', 'c', 'd'}, {'b', 'c', 'd'}, {'a', 'b', 'c', 'd'}
    ])
])
def test_power_set(input_set, power_set_expected):
    assert power_set(input_set) == set([frozenset(s) for s in power_set_expected])

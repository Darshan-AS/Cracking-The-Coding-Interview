"""
Parens: Implement an algorithm to print all valid (i.e., properly opened and closed) combinations of n pairs of
parentheses.
EXAMPLE:
    Input   : 3
    Output  : ((())) , (()()) , (())() , ()(()) , ()()()
"""
import pytest


def parens(n):
    parens_of_length = [{''}]
    
    if n == 0:
        return parens_of_length[n]
    
    # Generate all parens upto n
    for length in range(1, n + 1):
        parens_of_length.append(set())
        # Iterate i from start and j from end and find all possible pairs
        for i in range(length):
            j = length - i - 1
            # Use parens[i] as inside and parens[j] as outside
            for inside in parens_of_length[i]:
                for outside in parens_of_length[j]:
                    parens_of_length[length].add('(' + inside + ')' + outside)
                    
    return parens_of_length[n]


@pytest.mark.parametrize('n, parens_expected', [
    (0, {''}),
    (1, {'()'}),
    (2, {'(())', '()()'}),
    (3, {'((()))', '(()())', '(())()', '()(())', '()()()'})
])
def test_parens(n, parens_expected):
    assert parens(n) == parens_expected

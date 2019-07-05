"""
Boolean Evaluation: Given a boolean expression consisting of the symbols
0 (false),
1 (true),
& (AND),
| (OR),
^ (XOR),
and a desired boolean result value result,
implement a function to count the number of ways of parenthesizing the expression such that it evaluates to result.
The expression should be fully parenthesized (e.g., (0) ^ (1)) but not extraneously (e.g., (((0)) ^ (1))).

EXAMPLE
countEval('1 ^ 0 | 0 | 1', False) -> 2
countEval('0 & 0 & 0 & 1 ^ 1 | 0', true) -> 10
"""
import math

import pytest


def count_eval(expression, result, memo=None):
    # Calculates total number of ways to add parenthesis
    def catalan_number(n):
        return math.factorial(2 * n) / (math.factorial(n + 1) * math.factorial(n))
    
    if len(expression) == 1:
        return int(int(expression) == result)
    
    if memo is None:
        memo = {}
    elif expression in memo:
        return memo[expression][int(result)]

    true_ways = 0
    for i in range(1, len(expression) - 1, 2):
        # Divide at each operator and try all possible ways with result True
        left, operator, right = expression[:i], expression[i], expression[i + 1:]
        
        if operator == '&':
            true_ways += count_eval(left, True) * count_eval(right, True)
        elif operator == '|':
            true_ways += count_eval(left, True) * count_eval(right, True)
            true_ways += count_eval(left, True) * count_eval(right, False)
            true_ways += count_eval(left, False) * count_eval(right, True)
        elif operator == '^':
            true_ways += count_eval(left, True) * count_eval(right, False)
            true_ways += count_eval(left, False) * count_eval(right, True)
    
    total_ways = catalan_number((len(expression) - 1) / 2)
    false_ways = total_ways - true_ways
    memo[expression] = (false_ways, true_ways)
    
    return true_ways if result else false_ways
    

@pytest.mark.parametrize('expression, result, count_expected', [
    ('1', True, 1),
    ('0', True, 0),
    ('0', False, 1),
    ('1&1', True, 1),
    ('1|0', False, 0),
    ('1^0', True, 1),
    ('1&0&1', True, 0),
    ('1|1^0', True, 2),
    ('1^0|0|1', False, 2),
    ('1^0|0|1', True, 3),
    ('0&0&0&1^1|0', True, 10)
])
def test_count_eval(expression, result, count_expected):
    assert count_eval(expression, result) == count_expected

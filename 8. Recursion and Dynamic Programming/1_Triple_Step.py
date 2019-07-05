"""
Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
Implement a method to count how many possible ways the child can run up the stairs.
"""
import pytest


def triple_step(n):
    # Define base cases
    ways = [1, 1, 2]
    if n < 3:
        return ways[n]
    
    for i in range(3, n + 1):
        # Number of ways of reaching nth step is sum of ways of reaching n - 1, n - 2, n - 3 steps
        ways[i % 3] = sum(ways)
    return ways[n % 3]


@pytest.mark.parametrize('n, ways_expected', [
    (3, 4),
    (7, 44)
])
def test_triple_step(n, ways_expected):
    assert triple_step(n) == ways_expected

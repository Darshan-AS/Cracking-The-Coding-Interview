"""
Coins: Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent),
write code to calculate the number of ways of representing n cents.
"""
import pytest


def coins(n):
    denominations = [25, 10, 5, 1]
    memo = {}
    
    def coins_helper(amount, index):
        coin = denominations[index]
        if coin == 1 or len(denominations) == index + 1:
            return 1
        elif (amount, index) in memo:
            return memo[(amount, index)]
        
        ways = 0
        # Go to next denomination, assuming i coins of denomination amount
        for i in range(amount // coin + 1):
            ways += coins_helper(amount - i * coin, index + 1)
            
        memo[(amount, index)] = ways
        return ways
    
    return coins_helper(n, 0)


@pytest.mark.parametrize('n, ways_expected', [
    (0, 1),
    (1, 1),
    (4, 1),
    (5, 2),
    (15, 6),
    (17, 6),
    (20, 9),
    (25, 13),
    (52, 49)
])
def test_coins(n, ways_expected):
    assert coins(n) == ways_expected

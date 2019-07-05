"""
Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is, 617 + 295.
Output: 2 -> 1 -> 9. That is, 912.

FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is, 617 + 295.
Output: 9 -> 1 -> 2. That is, 912.
"""
import pytest

from LinkedList import LinkedList


def sum_lists(ll1, ll2):
    ll_sum = LinkedList()

    i, j = ll1.head, ll2.head
    carry = 0
    while i or j:
        value_sum = carry
        if i:
            value_sum += i.value
            i = i.next
        if j:
            value_sum += j.value
            j = j.next

        carry = value_sum // 10
        ll_sum.add(value_sum % 10)

    if carry:
        ll_sum.add(carry)
    return ll_sum


def sum_lists_follow_up(ll1, ll2):
    ll1_len, ll2_len = len(ll1), len(ll2)
    long, short = (ll1.head, ll2.head) if ll1_len > ll2_len else (ll2.head, ll1.head)

    value_sum = 0
    while ll1_len and ll2_len:
        value_sum = value_sum * 10
        if ll1_len == ll2_len:
            value_sum += long.value + short.value
            ll2_len -= 1
            short = short.next
        else:
            value_sum += long.value
        ll1_len -= 1
        long = long.next

    return LinkedList([int(i) for i in str(value_sum)])


@pytest.mark.parametrize('ll1, ll2, expected', [
    (LinkedList([7, 1, 6]), LinkedList([5, 9, 2]), LinkedList([2, 1, 9])),
    (LinkedList([9, 9]), LinkedList([1, 1]), LinkedList([0, 1, 1])),
    (LinkedList([0, 3, 9]), LinkedList([0, 8]), LinkedList([0, 1, 0, 1])),
])
def test_sum_lists(ll1, ll2, expected):
    assert sum_lists(ll1, ll2) == expected


@pytest.mark.parametrize('ll1, ll2, expected', [
    (LinkedList([6, 1, 7]), LinkedList([2, 9, 5]), LinkedList([9, 1, 2])),
    (LinkedList([9, 9]), LinkedList([1, 1]), LinkedList([1, 1, 0])),
    (LinkedList([9, 3, 0]), LinkedList([8, 0]), LinkedList([1, 0, 1, 0])),
])
def test_sum_lists_follow_up(ll1, ll2, expected):
    assert sum_lists_follow_up(ll1, ll2) == expected

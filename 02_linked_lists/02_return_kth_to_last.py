"""
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
"""
import pytest

from LinkedList import LinkedList


def return_kth_to_last(ll, k):
    if ll.head is None:
        return ll

    current, runner = ll.head, ll.head
    for i in range(k):
        if runner is None:
            return None
        runner = runner.next

    while runner:
        current, runner = current.next, runner.next

    return current.value


@pytest.mark.parametrize('ll, k, expected', [
    (LinkedList([1, 2, 8, 4, 7, 9, 3, 6, 1, 8, 0, 9]), 4, 1),
    (LinkedList([4, 6, 9, 2, 5, 0, 1]), 2, 0)
])
def test_return_kth_to_last(ll, k, expected):
    assert return_kth_to_last(ll, k) == expected

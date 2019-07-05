"""
Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node.
Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.
"""
import pytest

from LinkedList import LinkedList


def intersection(ll1, ll2):
    ll1_len, ll2_len = len(ll1), len(ll2)
    long, short = (ll1.head, ll2.head) if ll1_len > ll2_len else (ll2.head, ll1.head)
    
    for _ in range(abs(ll1_len - ll2_len)):
        long = long.next
    
    while long != short:
        long, short = long.next, short.next
    
    return long


@pytest.mark.parametrize('ll1, ll2, ll_common', [
    (LinkedList([3, 1, 5, 9]), LinkedList([4, 6]), LinkedList([7, 2, 1])),
    (LinkedList([3, 1, 5, 9, 7, 2, 1]), LinkedList([4, 6, 7, 2, 1]), LinkedList())
])
def test_intersection(ll1, ll2, ll_common):
    def get_tail(ll):
        current = ll.head
        while current.next:
            current = current.next
        return current
    
    get_tail(ll1).next = ll_common.head
    get_tail(ll2).next = ll_common.head

    assert intersection(ll1, ll2) == ll_common.head




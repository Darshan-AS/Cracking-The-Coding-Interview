"""
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""
import pytest

from linked_list import LinkedList


def partition(ll, x):
    left, right = ll.head, ll.head

    current = ll.head
    while current:
        next_node = current
        current = current.next

        if next_node.value < x:
            next_node.next = left
            left = next_node
        else:
            right.next = next_node
            right = next_node

    ll.head = left
    return ll


@pytest.mark.parametrize('ll, x', [
    (LinkedList([1, 2, 8, 4, 7, 9, 3, 6, 1, 8, 0, 9]), 5),
    (LinkedList([4, 6, 9, 2, 5, 0, 1]), 0)
])
def test_partition(ll, x):
    l = list(partition(ll, x))
    greater_started = False
    for i in l:
        if greater_started and i < x:
            assert False
        if i > x:
            greater_started = True
    assert True

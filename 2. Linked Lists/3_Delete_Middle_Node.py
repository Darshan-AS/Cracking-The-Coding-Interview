"""
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
lnput: the node c from the linked list a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f
"""
import pytest

from LinkedList import LinkedList


def delete_middle_node(kth_node):
    kth_node.value, kth_node.next = kth_node.next.value, kth_node.next.next


@pytest.mark.parametrize('ll, k, others, expected', [
    (LinkedList([1, 2, 8, 4, 7, 9]), 3, [6, 1, 8, 0, 9], LinkedList([1, 2, 8, 4, 7, 9, 6, 1, 8, 0, 9])),
    (LinkedList([4, 6, 9, 2, 5, 0]), 1, [2], LinkedList([4, 6, 9, 2, 5, 0, 2]))
])
def test_delete_middle_node(ll, k, others, expected):
    kth_node = ll.add(k)
    ll.add_all(others)
    delete_middle_node(kth_node)
    assert ll == expected

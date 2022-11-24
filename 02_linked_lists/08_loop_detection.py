"""
Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
as to make a loop in the linked list.
EXAMPLE
Input: A -> B -> C -> D -> E -> C [the same C as earlier]
Output: C
"""
import pytest

from LinkedList import LinkedList


def loop_detection(ll):
    slow_runner, fast_runner = ll.head, ll.head
    
    while fast_runner and fast_runner.next:
        fast_runner, slow_runner = fast_runner.next.next, slow_runner.next
        if fast_runner == slow_runner:
            break
    
    if fast_runner is None or fast_runner.next is None:
        return None
    
    fast_runner = ll.head
    while fast_runner != slow_runner:
        fast_runner, slow_runner = fast_runner.next, slow_runner.next
    
    return fast_runner


@pytest.mark.parametrize('ll1, ll2', [
    (LinkedList([3, 1, 5, 9]), LinkedList([4, 6])),
    (LinkedList([3, 1, 5, 9, 7, 2, 1]), LinkedList([4, 6, 7, 2, 1])),
    (LinkedList([1, 2, 3]), LinkedList())
])
def test_loop_detection(ll1, ll2):
    def get_tail(ll):
        current = ll.head
        while current.next:
            current = current.next
        return current
    
    if ll2.head:
        get_tail(ll1).next = ll2.head
        get_tail(ll2).next = ll2.head
    
    assert loop_detection(ll1) == ll2.head

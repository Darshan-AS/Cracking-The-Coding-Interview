"""
Remove Dups: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""
import pytest

from linked_list import LinkedList

"""
Time:   O(N)
Space:  O(N)
where,  N = length of ll
"""


def remove_duplicates(ll: LinkedList) -> LinkedList:
    if ll.head is None:
        return ll

    current = ll.head
    seen = {current.value}
    while current.next:
        # If already seen then remove
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next
    return ll


"""
Time:   O(N2)
Space:  O(1)
where,  N = length of ll
"""


def remove_duplicates_follow_up(ll: LinkedList) -> LinkedList:
    if ll.head is None:
        return ll

    walker = ll.head
    while walker.next:
        runner = walker
        # Remove all future nodes that have the same value
        while runner.next:
            if walker.value == runner.next.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        walker = walker.next

    return ll


@pytest.mark.parametrize('ll, no_duplicates_ll', [
    (LinkedList([1, 2, 8, 4, 7, 9, 3, 6, 1, 8, 0, 9]), LinkedList([1, 2, 8, 4, 7, 9, 3, 6, 0])),
    (LinkedList(), LinkedList())
])
def test_remove_duplicates(ll: LinkedList, no_duplicates_ll: LinkedList):
    assert remove_duplicates(ll) == no_duplicates_ll
    assert remove_duplicates_follow_up(ll) == no_duplicates_ll

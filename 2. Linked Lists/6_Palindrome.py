"""
Palindrome: Implement a function to check if a linked list is a palindrome.
"""
import pytest

from LinkedList import LinkedList


def palindrome(ll):
    stack = []
    
    current, runner = ll.head, ll.head
    while runner and runner.next:
        stack.append(current.value)
        current, runner = current.next, runner.next.next
        
    if runner:
        current = current.next
    
    while current:
        if current.value != stack.pop():
            return False
        current = current.next
    return True


@pytest.mark.parametrize('ll, expected', [
    (LinkedList([1, 2, 3, 4, 5, 4, 3, 2, 1]), True),
    (LinkedList([1, 2, 3, 4, 5, 5, 4, 3, 2, 1]), True),
    (LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9]), False)
])
def test_palindrome(ll, expected):
    assert palindrome(ll) == expected

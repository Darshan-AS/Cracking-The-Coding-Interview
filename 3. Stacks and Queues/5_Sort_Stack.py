"""
Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and is_empty.
"""
from Stack import Stack


def sort_stack(stack):
    if len(stack) <= 1:
        return stack
    
    sorted_stack = Stack(stack.capacity)
    while not stack.is_empty():
        next_value = stack.pop()
        while sorted_stack.peek() is not None and next_value > sorted_stack.peek():
            stack.push(sorted_stack.pop())
        sorted_stack.push(next_value)
    return sorted_stack


def test_sort_stack():
    stack = Stack(5)
    stack.push(3)
    stack.push(2)
    stack.push(4)
    stack.push(1)
    stack.push(5)
    
    sorted_stack = sort_stack(stack)
    assert sorted_stack.pop() == 1
    assert sorted_stack.pop() == 2
    assert sorted_stack.pop() == 3
    assert sorted_stack.pop() == 4
    assert sorted_stack.pop() == 5

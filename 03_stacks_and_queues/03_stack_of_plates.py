"""
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
(that is, pop () should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt (int index) which performs a pop operation on a specific sub-stack.
"""
import pytest
from stack import Stack


class StackOfPlates:
    
    def __init__(self, each_stack_capacity):
        self.each_stack_capacity = each_stack_capacity
        self.stacks = []
    
    def push(self, value):
        if not self.stacks or self.stacks[-1].is_full():
            self.stacks.append(Stack(capacity=self.each_stack_capacity))
        self.stacks[-1].push(value)
    
    def pop(self):
        if not self.stacks:
            raise Exception('Stacks Underflow')
        
        if self.stacks[-1].is_empty():
            self.stacks.pop()
        return self.stacks[-1].pop()
    
    def pop_at(self, stack_number):
        if stack_number >= len(self.stacks):
            raise Exception('Stack Not Found')
        
        value = self.stacks[stack_number].pop()
        self.shift_stacks(stack_number)
        return value
    
    def shift_stacks(self, stack_number):
        if stack_number == len(self.stacks) - 1:
            return
        
        reverse_stack = Stack(capacity=self.each_stack_capacity)
        next_stack = self.stacks[stack_number + 1]
        while not next_stack.is_empty():
            reverse_stack.push(next_stack.pop())
        
        self.stacks[stack_number].push(reverse_stack.pop())
        self.shift_stacks(stack_number + 1)


def test_stack_of_plates():
    stack = StackOfPlates(3)
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    stack.push(4)
    stack.push(5)
    stack.push(6)
    
    stack.push(7)
    
    assert stack.pop() == 7
    assert stack.pop() == 6
    
    with pytest.raises(Exception) as e:
        stack.pop_at(2)
    assert str(e.value) == 'Stack Not Found'
    
    assert stack.pop_at(1) == 5
    assert stack.pop_at(0) == 3

test_stack_of_plates()

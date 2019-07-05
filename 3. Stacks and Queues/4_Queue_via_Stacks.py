"""
Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks
"""
import pytest
from Stack import Stack


class QueueViaStacks:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.add_stack = Stack(self.capacity)
        self.delete_stack = Stack(self.capacity)
    
    def __len__(self):
        return len(self.add_stack) + len(self.delete_stack)
    
    def add(self, value):
        if len(self) == self.capacity:
            raise Exception('Queue Overflow')
        self.add_stack.push(value)
    
    def delete(self):
        if len(self) == 0:
            raise Exception('Queue Underflow')
        
        if self.delete_stack.is_empty():
            self.shift_stacks()
        return self.delete_stack.pop()

    def shift_stacks(self):
        while not self.add_stack.is_empty():
            self.delete_stack.push(self.add_stack.pop())


def test_queue_via_stacks():
    queue = QueueViaStacks(5)
    
    queue.add(1)
    queue.add(2)
    queue.add(3)
    assert queue.delete() == 1
    
    queue.add(4)
    queue.add(5)
    queue.add(6)
    
    with pytest.raises(Exception) as e:
        queue.add(7)
    assert str(e.value) == 'Queue Overflow'
    
    assert queue.delete() == 2
    assert queue.delete() == 3
    assert queue.delete() == 4
    assert queue.delete() == 5
    assert queue.delete() == 6
    
    with pytest.raises(Exception) as e:
        queue.delete()
    assert str(e.value) == 'Queue Underflow'

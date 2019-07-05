"""
Three in One: Describe how you could use a single array to implement three stacks.
"""
import pytest


class MultiStack:
    
    def __init__(self, size, n):
        self.space = [None] * size
        self.index = list(range(1, size)) + [None]
        self.tops = [None] * (n + 1)
        self.next_available_index = 0
    
    def push(self, value, stack_number):
        if self.next_available_index is None:
            raise Exception('Stack Overflow')
        
        next_available_index = self.index[self.next_available_index]
        
        self.space[self.next_available_index] = value
        self.index[self.next_available_index] = self.tops[stack_number]
        self.tops[stack_number] = self.next_available_index
        self.next_available_index = next_available_index
    
    def pop(self, stack_number):
        if self.tops[stack_number] is None:
            raise Exception('Stack Underflow')
        
        value = self.space[self.tops[stack_number]]
        previous_used_index = self.index[self.tops[stack_number]]
        
        self.space[self.tops[stack_number]] = None
        self.index[self.tops[stack_number]] = self.next_available_index
        self.next_available_index = self.tops[stack_number]
        self.tops[stack_number] = previous_used_index
        
        return value


def test_three_in_one():
    multi_stack = MultiStack(10, 3)
    multi_stack.push(1, 1)
    multi_stack.push(2, 1)
    
    multi_stack.push(3, 2)
    multi_stack.push(4, 2)
    assert multi_stack.pop(1) == 2
    multi_stack.push(5, 2)
    multi_stack.push(6, 2)
    multi_stack.push(7, 2)
    
    multi_stack.push(8, 3)
    multi_stack.push(9, 3)
    multi_stack.push(10, 3)
    
    multi_stack.push(11, 2)
    with pytest.raises(Exception) as e:
        multi_stack.push(12, 2)
    assert str(e.value) == 'Stack Overflow'
    
    assert multi_stack.pop(3) == 10
    assert multi_stack.pop(1) == 1
    with pytest.raises(Exception) as e:
        multi_stack.pop(1)
    assert str(e.value) == 'Stack Underflow'

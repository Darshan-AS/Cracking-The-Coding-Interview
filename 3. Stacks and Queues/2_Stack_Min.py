"""
Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time
"""
import pytest


class StackWithMin:
    
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        if self.stack:
            self.stack.append((value, min(value, self.stack[-1][1])))
            return
        self.stack.append((value, value))
    
    def pop(self):
        if self.stack:
            return self.stack.pop()[0]
        raise Exception('Stack Underflow')
    
    def min(self):
        if self.stack:
            return self.stack[-1][1]
        return None


def test_stack_min():
    stack = StackWithMin()
    assert stack.min() is None
    
    stack.push(5)
    assert stack.min() == 5
    
    stack.push(6)
    assert stack.min() == 5
    
    stack.push(3)
    assert stack.min() == 3
    
    stack.push(7)
    assert stack.min() == 3
    
    assert stack.pop() == 7
    assert stack.min() == 3
    
    assert stack.pop() == 3
    assert stack.min() == 5
    
    assert stack.pop() == 6
    assert stack.min() == 5
    
    assert stack.pop() == 5
    assert stack.min() is None
    
    with pytest.raises(Exception) as e:
        stack.pop()
    assert str(e.value) == 'Stack Underflow'

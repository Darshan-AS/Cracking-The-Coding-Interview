class Stack:
    
    def __init__(self, stack=None, capacity=10):
        self.capacity = capacity
        self.top = None
        self.stack = stack if stack else [None] * self.capacity
    
    def __iter__(self):
        top = self.top
        while top is not None and top >= 0:
            yield self.stack[top]
            top -= 1
    
    def __repr__(self):
        values = [str(i) for i in self]
        return 'Stack: top -> ' + ' - '.join(values)
    
    def __len__(self):
        return 0 if self.top is None else self.top + 1
    
    def __eq__(self, other):
        return self.stack[:self.top + 1] == other.stack[:other.top + 1]
    
    def is_empty(self):
        return self.top is None
    
    def is_full(self):
        return self.top == self.capacity - 1
    
    def push(self, value):
        if self.is_full():
            raise Exception('Stack Overflow')
        
        self.top = 0 if self.top is None else self.top + 1
        self.stack[self.top] = value
    
    def pop(self):
        if self.is_empty():
            raise Exception('Stack Underflow')
        
        value = self.stack[self.top]
        self.stack[self.top] = None
        self.top = None if self.top == 0 else self.top - 1
        return value
    
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[self.top]

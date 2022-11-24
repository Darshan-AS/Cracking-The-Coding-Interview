class Queue:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.head, self.tail = None, None
        self.queue = [None] * self.capacity
    
    def __iter__(self):
        if self.head is None or self.tail is None:
            return
        
        head = self.head
        while head != self.tail:
            yield self.queue[head]
            head = (head + 1) % self.capacity
        yield self.queue[head]
    
    def __repr__(self):
        values = [str(i) for i in self]
        return 'Queue: head -> ' + ' - '.join(values) + ' <- tail'
    
    def __len__(self):
        if self.head is None or self.tail is None:
            return 0
        
        if self.tail >= self.head:
            return self.tail - self.head + 1
        else:
            return self.tail + self.capacity - self.head + 1
    
    def is_empty(self):
        return self.head is None and self.tail is None
    
    def is_full(self):
        return (self.tail + 1) % self.capacity == self.head
    
    def enqueue(self, value):
        if self.tail is None:
            self.head, self.tail = 0, 0
        elif self.is_full():
            raise Exception('Queue Overflow')
        else:
            self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = value
    
    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue Underflow')
        
        value = self.queue[self.head]
        
        if self.head == self.tail:
            self.head, self.tail = None, None
        else:
            self.head = (self.head + 1) % self.capacity
        return value
    
    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]
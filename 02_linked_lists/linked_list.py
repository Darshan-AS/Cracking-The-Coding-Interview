class LinkedListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node
    
    def __repr__(self):
        return str(self.value)


class LinkedList:
    
    def __init__(self, values=None):
        self.head = None
        if values:
            self.add_all(values)
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next
    
    def __eq__(self, other):
        return list(self) == list(other)
    
    def __repr__(self):
        values = [str(i) for i in self]
        return 'Singly Linked List: ' + ' -> '.join(values)
    
    def __len__(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length
    
    def add(self, value):
        if self.head is None:
            self.head = LinkedListNode(value)
            return self.head
        
        current = self.head
        while current.next:
            current = current.next
        current.next = LinkedListNode(value)
        return current.next
    
    def add_first(self, value):
        if self.head is None:
            self.head = LinkedListNode(value)
            return self.head
        
        node = LinkedListNode(value)
        node.next, self.head = self.head, node
        return self.head
    
    def add_all(self, values):
        for value in values:
            self.add(value)
    
    def delete(self, value):
        if self.head.value == value:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

class BinarySearchTree:
    class Node:
        
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right
            self.parent = None
            
            if self.left:
                self.left.parent = self
            if self.right:
                self.right.parent = self
        
        def __repr__(self):
            l = str(self.left.value) if self.left else ''
            r = str(self.right.value) if self.right else ''
            return f'{self.value}: [{l}, {r}]\n' + '\n'.join([str(self.left), str(self.right)])
    
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, value):
        self.root = BinarySearchTree.__insert(self.root, value)
    
    @staticmethod
    def __insert(root, value):
        if root is None:
            return BinarySearchTree.Node(value)
        
        if value < root.value:
            root.left = BinarySearchTree.__insert(root.left, value)
        else:
            root.right = BinarySearchTree.__insert(root.right, value)
        
        return root
    
    def __repr__(self):
        return repr(self.root)

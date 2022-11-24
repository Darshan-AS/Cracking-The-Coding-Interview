class BinaryTree:
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
        
        def inorder(self):
            if self.left:
                yield from self.left.inorder()
            
            yield self.value
            
            if self.right:
                yield from self.right.inorder()
        
        def preorder(self):
            yield self.value
            
            if self.left:
                yield from self.left.preorder()
            
            if self.right:
                yield from self.right.preorder()
        
        def postorder(self):
            if self.left:
                yield from self.left.postorder()
            
            if self.right:
                yield from self.right.postorder()
            
            yield self.value
    
    def __init__(self, root=None):
        self.root = root
    
    def __repr__(self):
        return repr(self.root)

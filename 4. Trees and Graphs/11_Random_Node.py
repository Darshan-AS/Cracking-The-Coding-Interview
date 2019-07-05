"""
Random Node: You are implementing a binary tree class from scratch which, in addition to
insert, find, and delete, has a method getRandomNode() which returns a random node
from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
for getRandomNode, and explain how you would implement the rest of the methods.
"""
from random import randint

from BinaryTree import BinaryTree


class BinaryTreeExtended(BinaryTree):
    class NodeExtended(BinaryTree.Node):
        
        def __init__(self, value, left=None, right=None):
            super().__init__(value, left, right)
            self.size = 1
            if self.left:
                self.size += len(self.left)
            if self.right:
                self.size += len(self.right)
        
        def __len__(self):
            return self.size
    
    def __len__(self):
        return len(self.root)
    
    def get_random_node(self):
        random_number = randint(0, len(self))
        return BinaryTreeExtended.get_node_at(self.root, random_number)
    
    @staticmethod
    def get_node_at(node, inorder_index):
        if inorder_index == 0:
            return node
        if node.left:
            if len(node.left) >= inorder_index:
                return BinaryTreeExtended.get_node_at(node.left, inorder_index - 1)
            elif node.right:
                return BinaryTreeExtended.get_node_at(node.right, inorder_index - len(node.left) - 1)
        if node.right:
            return BinaryTreeExtended.get_node_at(node.right, inorder_index - 1)


def test_get_node_at():
    b = BinaryTreeExtended(BinaryTreeExtended.NodeExtended(11, BinaryTreeExtended.NodeExtended(21, BinaryTreeExtended.NodeExtended(31),
        BinaryTreeExtended.NodeExtended(32, BinaryTreeExtended.NodeExtended(41), BinaryTreeExtended.NodeExtended(42, None,
        BinaryTreeExtended.NodeExtended(51)))), BinaryTreeExtended.NodeExtended(22, BinaryTreeExtended.NodeExtended(33),
        BinaryTreeExtended.NodeExtended(34))))
    
    assert b.get_node_at(b.root, 0).value == 11
    assert b.get_node_at(b.root, 4).value == 41
    assert b.get_node_at(b.root, 8).value == 33

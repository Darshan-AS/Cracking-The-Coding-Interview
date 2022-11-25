"""
Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent.
"""

from binary_search_tree import BinarySearchTree


def successor(node):
    if node is None:
        return
    
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    
    parent = node.parent
    while parent and parent.right == node:
        node, parent = parent, parent.parent
    
    return parent


def test_successor():
    node_1 = BinarySearchTree.Node(1)
    node_3 = BinarySearchTree.Node(3)
    node_2 = BinarySearchTree.Node(2, node_1, node_3)
    node_5 = BinarySearchTree.Node(5)
    node_7 = BinarySearchTree.Node(7)
    node_6 = BinarySearchTree.Node(6, node_5, node_7)
    node_4 = BinarySearchTree.Node(4, node_2, node_6)
    
    assert successor(node_1) == node_2
    assert successor(node_2) == node_3
    assert successor(node_3) == node_4
    assert successor(node_4) == node_5
    assert successor(node_5) == node_6
    assert successor(node_6) == node_7
    assert successor(node_7) is None

"""
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
"""

from BinaryTree import BinaryTree
from LinkedList import LinkedList


def list_of_depth(root):
    depth_lists = []
    if root is None:
        return depth_lists
    
    depth_lists.append(LinkedList([root]))
    while True:
        current_list = depth_lists[-1]
        next_list = []
        for node in current_list:
            if node.left:
                next_list.append(node.left)
            if node.right:
                next_list.append(node.right)
        if len(next_list):
            depth_lists.append(next_list)
        else:
            break
    return depth_lists


def test_list_of_depths():
    node_7 = BinaryTree(7)
    node_6 = BinaryTree(6)
    node_5 = BinaryTree(5)
    node_4 = BinaryTree(4)
    node_3 = BinaryTree(3, node_6, node_7)
    node_2 = BinaryTree(2, node_4, node_5)
    root = BinaryTree(1, node_2, node_3)
    
    depth_lists = [LinkedList([root]), LinkedList([node_2, node_3]), LinkedList([node_4, node_5, node_6, node_7])]
    assert list_of_depth(root) == depth_lists

"""
Validate BST: Implement a function to check if a binary tree is a binary search tree.
"""
import pytest

from binary_tree import BinaryTree


def validate_bst_node(node, left_bound, right_bound):
    if node is None:
        return True
    
    return left_bound <= node.value < right_bound and validate_bst_node(node.left,
                                                                        left_bound,
                                                                        node.value) and validate_bst_node(node.right,
                                                                                                          node.value,
                                                                                                          right_bound)


def validate_bst(root):
    return validate_bst_node(root, -float('inf'), float('inf'))


@pytest.mark.parametrize('binary_tree, expected', [
    (BinaryTree.Node(10, BinaryTree.Node(5, BinaryTree.Node(2), BinaryTree.Node(7)), BinaryTree.Node(15, BinaryTree.Node(12), BinaryTree.Node(17))), True),
    (BinaryTree.Node(1, BinaryTree.Node(0, BinaryTree.Node(-1, BinaryTree.Node(-2)))), True),
    (BinaryTree.Node(5, BinaryTree.Node(3, BinaryTree.Node(2), BinaryTree.Node(6)), BinaryTree.Node(10)), False)
])
def test_validate_bst(binary_tree, expected):
    assert validate_bst(binary_tree) == expected

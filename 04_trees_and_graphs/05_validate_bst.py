"""
Validate BST: Implement a function to check if a binary tree is a binary search tree.
"""
import pytest

from BinaryTree import BinaryTree


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
    (BinaryTree(10, BinaryTree(5, BinaryTree(2), BinaryTree(7)), BinaryTree(15, BinaryTree(12), BinaryTree(17))), True),
    (BinaryTree(1, BinaryTree(0, BinaryTree(-1, BinaryTree(-2)))), True),
    (BinaryTree(5, BinaryTree(3, BinaryTree(2), BinaryTree(6)), BinaryTree(10)), False)
])
def test_validate_bst(binary_tree, expected):
    assert validate_bst(binary_tree) == expected

"""
Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.
"""
import pytest

from binary_tree import BinaryTree


def check_balanced(node):
    if node is None:
        return True, -1
    left_balanced, left_height = check_balanced(node.left)
    right_balanced, right_height = check_balanced(node.right)
    
    if not left_balanced or not right_balanced or abs(left_height - right_height) > 1:
        return False, max(left_height, right_height) + 1
    
    return True, max(left_height, right_height) + 1


@pytest.mark.parametrize('binary_tree, expected', [
    (BinaryTree.Node(1), (True, 0)),
    (BinaryTree.Node(1, BinaryTree.Node(2, BinaryTree.Node(4), BinaryTree.Node(5)), BinaryTree.Node(3, BinaryTree.Node(6), BinaryTree.Node(7, BinaryTree.Node(8)))), (True, 3)),
    (BinaryTree.Node(1, BinaryTree.Node(2, BinaryTree.Node(3, BinaryTree.Node(4))), BinaryTree.Node(5)), (False, 3))
])
def test_check_balanced(binary_tree, expected):
    assert check_balanced(binary_tree) == expected

"""
Check Subtree: T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an
algorithm to determine if T2 is a subtree of T1.
A tree T2 is a subtree of Tl if there exists a node n in T1 such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical.
"""
import pytest

from binary_tree import BinaryTree


def match_tree(t1, t2):
    if t1 is None and t2 is None:
        return True
    elif t1 is None or t2 is None:
        return False
    
    return t1.value == t2.value and match_tree(t1.left, t2.left) and match_tree(t1.right, t2.right)


def is_sub_tree(large_tree, small_tree):
    if not large_tree:
        return False
    elif match_tree(large_tree, small_tree):
        return True
    
    return is_sub_tree(large_tree.left, small_tree) or is_sub_tree(large_tree.right, small_tree)


@pytest.mark.parametrize('large_tree, small_tree, expected_is_sub_tree', [
    (BinaryTree.Node(5, BinaryTree.Node(3, BinaryTree.Node(2), BinaryTree.Node(4)),
                BinaryTree.Node(8, BinaryTree.Node(7, BinaryTree.Node(9)), BinaryTree.Node(1))),
     BinaryTree.Node(8, BinaryTree.Node(7), BinaryTree.Node(1)),
     False),
    (BinaryTree.Node(5, BinaryTree.Node(3, BinaryTree.Node(2), BinaryTree.Node(4)),
                BinaryTree.Node(8, BinaryTree.Node(7, BinaryTree.Node(9)), BinaryTree.Node(1))),
     BinaryTree.Node(8, BinaryTree.Node(7, BinaryTree.Node(9)), BinaryTree.Node(1)),
     True)
])
def test_is_sub_tree(large_tree, small_tree, expected_is_sub_tree):
    assert is_sub_tree(large_tree, small_tree) == expected_is_sub_tree

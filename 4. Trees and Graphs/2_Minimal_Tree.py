"""
Minimal Tree: Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.
"""
import pytest

from BinarySearchTree import BinarySearchTree


def minimal_tree(sorted_list):
    if not sorted_list:
        return
    
    mid = len(sorted_list) // 2
    left = minimal_tree(sorted_list[:mid])
    right = minimal_tree(sorted_list[mid + 1:])
    return BinarySearchTree.Node(sorted_list[mid], left, right)


@pytest.mark.parametrize('sorted_list, expected', [
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4),
    ([2, 4, 6, 8, 10, 12, 14], 3)
])
def test_minimal_tree(sorted_list, expected):
    def height(node):
        if node is None:
            return 0
        return max(height(node.left), height(node.right)) + 1
    
    root = minimal_tree(sorted_list)
    assert height(root) == expected

"""
Paths with Sum: You are given a binary tree in which each node contains an integer value (which
might be positive or negative). Design an algorithm to count the number of paths that sum to a
given value. The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).
"""
from collections import defaultdict

from binary_tree import BinaryTree


def paths_with_sum_helper(node, target_sum, running_sum, running_sum_map):
    if not node:
        return 0
    
    running_sum += node.value
    running_sum_pair = running_sum - target_sum
    path_count = running_sum_map[running_sum_pair]
    
    if running_sum == target_sum:
        path_count += 1
    
    running_sum_map[running_sum] += 1
    path_count += paths_with_sum_helper(node.left, target_sum, running_sum, running_sum_map)
    path_count += paths_with_sum_helper(node.right, target_sum, running_sum, running_sum_map)
    running_sum_map[running_sum] -= 1
    
    return path_count


def paths_with_sum(bt, target_sum):
    return paths_with_sum_helper(bt, target_sum, 0, defaultdict(int))


def test_paths_with_sum():
    b = BinaryTree.Node(4, BinaryTree.Node(-2, BinaryTree.Node(7), BinaryTree.Node(4)),
                        BinaryTree.Node(7, BinaryTree.Node(-1, BinaryTree.Node(-1),
                                                           BinaryTree.Node(2, BinaryTree.Node(1))),
                                        BinaryTree.Node(0, None, BinaryTree.Node(-2))))
    assert paths_with_sum(b, 12) == 1
    assert paths_with_sum(b, 2) == 4
    assert paths_with_sum(b, 9) == 4

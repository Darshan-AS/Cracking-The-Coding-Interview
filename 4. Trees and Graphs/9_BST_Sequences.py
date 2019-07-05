"""
BST Sequences: A binary search tree was created by traversing through an array from left to right
and inserting each element. Given a binary search tree with distinct elements, print all possible
arrays that could have led to this tree.
EXAMPLE
Input:
          2
        /   \
       1     3
Output: {2, 1, 3}, {2, 3, 1}
"""
import pytest

from BinarySearchTree import BinarySearchTree


def all_possible_bst_sequences_helper(prefix, sub_bsts):
    if not len(sub_bsts):
        return [prefix]
    
    possible_sequences = []
    for index, sub_bst in enumerate(sub_bsts):
        next_prefix = prefix + [sub_bst.value]
        remaining_sub_bsts = sub_bsts[:index] + sub_bsts[index + 1:]
        
        if sub_bst.left:
            remaining_sub_bsts.append(sub_bst.left)
        if sub_bst.right:
            remaining_sub_bsts.append(sub_bst.right)
        
        possible_sequences += all_possible_bst_sequences_helper(next_prefix, remaining_sub_bsts)
    
    return possible_sequences


def all_possible_bst_sequences(bst):
    return all_possible_bst_sequences_helper([], [bst])


@pytest.mark.parametrize('bst, expected_possible_sequences', [
    (BinarySearchTree.Node(2, BinarySearchTree.Node(1), BinarySearchTree.Node(3)), [
        [2, 1, 3],
        [2, 3, 1]
    ]),
    (BinarySearchTree.Node(7, BinarySearchTree.Node(4, BinarySearchTree.Node(5)), BinarySearchTree.Node(9)), [
        [7, 4, 9, 5],
        [7, 4, 5, 9],
        [7, 9, 4, 5]
    ]),
    ((BinarySearchTree.Node(7, BinarySearchTree.Node(4, BinarySearchTree.Node(5), BinarySearchTree.Node(6)),
                            BinarySearchTree.Node(9))), [
         [7, 4, 9, 5, 6],
         [7, 4, 9, 6, 5],
         [7, 4, 5, 9, 6],
         [7, 4, 5, 6, 9],
         [7, 4, 6, 9, 5],
         [7, 4, 6, 5, 9],
         [7, 9, 4, 5, 6],
         [7, 9, 4, 6, 5]
     ])

])
def test_all_possible_bst_sequences(bst, expected_possible_sequences):
    assert all_possible_bst_sequences(bst) == expected_possible_sequences

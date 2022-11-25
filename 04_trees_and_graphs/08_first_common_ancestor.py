"""
First Common Ancestor: Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree.
"""

from binary_tree import BinaryTree


def first_common_ancestor(node_1, node_2):
    def get_depth(node):
        depth = 0
        while node.parent:
            node = node.parent
            depth += 1
        return depth
    
    node_1_depth, node_2_depth = get_depth(node_1), get_depth(node_2)
    deep_node, shallow_node = (node_1, node_2) if node_1_depth > node_2_depth else (node_2, node_1)
    
    for _ in range(abs(node_1_depth - node_2_depth)):
        deep_node = deep_node.parent
    
    while deep_node != shallow_node:
        deep_node, shallow_node = deep_node.parent, shallow_node.parent
    
    return deep_node


def test_first_common_ancestor():
    node_1 = BinaryTree.Node(1)
    node_3 = BinaryTree.Node(3)
    node_2 = BinaryTree.Node(2, node_1, node_3)
    node_5 = BinaryTree.Node(5)
    node_7 = BinaryTree.Node(7)
    node_6 = BinaryTree.Node(6, node_5, node_7)
    node_4 = BinaryTree.Node(4, node_2, node_6)
    
    assert first_common_ancestor(node_1, node_2) == node_2
    assert first_common_ancestor(node_1, node_3) == node_2
    assert first_common_ancestor(node_1, node_4) == node_4
    assert first_common_ancestor(node_1, node_5) == node_4
    assert first_common_ancestor(node_1, node_6) == node_4
    assert first_common_ancestor(node_1, node_7) == node_4
    assert first_common_ancestor(node_2, node_3) == node_2
    assert first_common_ancestor(node_2, node_4) == node_4
    assert first_common_ancestor(node_2, node_5) == node_4
    assert first_common_ancestor(node_2, node_6) == node_4
    assert first_common_ancestor(node_2, node_7) == node_4
    assert first_common_ancestor(node_3, node_4) == node_4
    assert first_common_ancestor(node_3, node_5) == node_4
    assert first_common_ancestor(node_3, node_6) == node_4
    assert first_common_ancestor(node_3, node_7) == node_4
    assert first_common_ancestor(node_4, node_5) == node_4
    assert first_common_ancestor(node_4, node_6) == node_4
    assert first_common_ancestor(node_4, node_7) == node_4
    assert first_common_ancestor(node_5, node_6) == node_6
    assert first_common_ancestor(node_5, node_7) == node_6
    assert first_common_ancestor(node_6, node_7) == node_6

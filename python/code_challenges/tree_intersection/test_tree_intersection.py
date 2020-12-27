from .tree_intersection import value_tree, BinaryTree, Node
import pytest

def test_proof_tree():
    assert value_tree
    assert BinaryTree

def test_happy_path():
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    tree1.root = Node(1)
    tree1.root.left = Node(2)
    tree1.root.right = Node(3)
    tree1.root.left.left = Node(4)
    tree1.root.left.right = Node(5)
    tree2.root = Node(1)
    tree2.root.left = Node(2)
    tree2.root.right = Node(3)
    tree2.root.left.left = Node(20)
    tree2.root.left.right = Node(5)
    actual = value_tree(tree1, tree2)
    expected = set([1, 2, 3, 5])
    assert actual == expected

def test_angry_path():
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    tree1.root = Node(1)
    tree1.root.left = Node(2)
    tree1.root.right = Node(3)
    tree1.root.left.left = Node(4)
    tree1.root.left.right = Node(5)
    tree2.root = Node(1)
    tree2.root.left = Node(2)
    tree2.root.right = Node(3)
    actual = value_tree(tree1, tree2)
    expected = set([1, 2, 3, 8])
    assert actual != expected

def test_different_length_trees():
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    tree1.root = Node(1)
    tree1.root.left = Node(2)
    tree1.root.right = Node(3)
    tree1.root.left.left = Node(4)
    tree1.root.left.right = Node(5)
    tree2.root = Node(1)
    tree2.root.left = Node(2)
    tree2.root.right = Node(3)
    actual = value_tree(tree1, tree2)
    expected = set([1, 2, 3])
    assert actual == expected


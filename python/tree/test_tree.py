from tree import BinarySearchTree, BinaryTree, Node


def test_instantiate_empty_tree():
    tree = BinaryTree()
    assert tree.root is None


def test_instantiate_single_root():
    tree = BinarySearchTree()
    tree.add(1)
    assert tree.root.value == 1


def test_add_to_left():
    tree = BinarySearchTree()
    tree.add(3)
    tree.add(2)
    tree.add(6)
    assert tree.root.left.value == 2


def test_add_to_right():
    tree = BinarySearchTree()
    tree.add(3)
    tree.add(2)
    tree.add(6)
    assert tree.root.right.value == 6


def test_return_preorder_traversal():
    tree = BinarySearchTree()
    traverse = BinaryTree()
    tree.add(3)
    tree.add(2)
    tree.add(6)
    actual = tree.pre_order()
    expected = [3,2,6]
    assert actual == expected

def test_return_inorder_traversal():
    tree = BinarySearchTree()
    traverse = BinaryTree()
    tree.add(3)
    tree.add(2)
    tree.add(6)
    actual = tree.in_order()
    expected = [2,3,6]
    assert actual == expected


def test_return_postorder_traversal():
    tree = BinarySearchTree()
    tree.add(3)
    tree.add(2)
    tree.add(6)
    actual = tree.post_order()
    expected = [2,6,3]
    assert actual == expected


## Code Challenge 17 tests:

def test_happy_maximum():
    tree = BinaryTree()
    Node1 = Node(7)
    Node2 = Node(8)
    Node3 = Node(788)
    Node1.left = Node2
    Node1.right = Node3
    tree.root = Node1
    actual = tree.find_maximum_value()
    expected = 788
    assert actual == expected


def test_edge_negative_maxiumum():
    tree = BinaryTree()
    Node1 = Node(-7)
    Node2 = Node(-8)
    Node3 = Node(-78)
    Node1.left = Node2
    Node1.right = Node3
    tree.root = Node1
    actual = tree.find_maximum_value()
    expected = -7
    assert actual == expected

def test_empty_maximum():
    tree = BinaryTree()
    actual = tree.find_maximum_value()
    expected = "I pitty the empty fool!"
    assert actual == expected

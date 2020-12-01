from tree import BinaryTree, BinarySearchTree


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
    traverse = BinaryTree()
    tree.add(3)
    tree.add(2)
    tree.add(6)
    actual = tree.post_order()
    expected = [2,6,3]
    assert actual == expected

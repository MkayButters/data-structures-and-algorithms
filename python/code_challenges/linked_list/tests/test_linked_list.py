import pytest

from linked_list import LinkedList

def test_import():
    assert LinkedList

def test_instantiate_list():
    empty_list = LinkedList()
    assert empty_list.head == None


def test_insert_into_list():
    new_list = LinkedList()
    new_list.insert("abcd")
    assert new_list.head.value == "abcd"

def test_head_pointer():
    new_list = LinkedList()
    new_list.insert("a")
    new_list.insert("b")
    new_list.insert("c")
    assert new_list.head.value == "c"

def test_insert_multiple_nodes():
    new_list = LinkedList()
    new_list.insert("a")
    new_list.insert("b")
    new_list.insert("c")
    assert new_list.head.next.value == "b"
    assert new_list.head.next.next.value == "a"

def test_return_true_onfind():
    find_items = LinkedList()
    find_items.insert("d")
    find_items.insert("e")
    find_items.insert("f")
    find_items.insert("g")
    find_items.insert("h")
    assert find_items.includes("d")

def test_return_false():
    find_items = LinkedList()
    find_items.insert("d")
    find_items.insert("e")
    find_items.insert("f")
    find_items.insert("g")
    find_items.insert("h")
    assert not find_items.includes("alskjfdlkjsfdfdsljk")


def test_return_collection():
    collection = LinkedList()
    collection.insert("c")
    collection.insert("b")
    collection.insert("a")
    expected = "{ a } -> { b } -> { c } -> NULL"
    assert expected == collection.__str__()


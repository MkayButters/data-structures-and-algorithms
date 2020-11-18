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

#Challenge 6 tests

def test_append_one():
    append_one = LinkedList()
    append_one.append("last one")
    actual = append_one.head.value
    expected = "last one"
    assert actual == expected

def test_append_multiple():
    append_many = LinkedList()
    append_many.insert("c")
    append_many.insert("b")
    append_many.insert("a")
    append_many.append("d")
    append_many.append("e")
    append_many.append("f")
    append_many.append("g")
    actual = str(append_many)
    expected = "{ a } -> { b } -> { c } -> { d } -> { e } -> { f } -> { g } -> NULL"
    assert actual == expected

def test_before_middle():
    make_list = LinkedList()
    make_list.insert(3)
    make_list.insert(1)
    make_list.append(5)
    make_list.append(11)
    make_list.append(3)
    make_list.insertBefore(5,8)
    actual = str(make_list)
    expected = "{ 1 } -> { 3 } -> { 8 } -> { 5 } -> { 11 } -> { 3 } -> NULL"
    assert actual == expected

def test_before_first():
    make_list = LinkedList()
    make_list.insert(3)
    make_list.insert(1)
    make_list.append(5)
    make_list.append(11)
    make_list.append(3)
    make_list.insertBefore(1,8)
    actual = str(make_list)
    expected = "{ 8 } -> { 1 } -> { 3 } -> { 5 } -> { 11 } -> { 3 } -> NULL"
    assert actual == expected

def test_after_middle():
    make_list = LinkedList()
    make_list.insert(3)
    make_list.insert(1)
    make_list.append(5)
    make_list.append(11)
    make_list.append(3)
    make_list.insertAfter(5,8)
    actual = str(make_list)
    expected = "{ 1 } -> { 3 } -> { 5 } -> { 8 } -> { 11 } -> { 3 } -> NULL"
    assert actual == expected


def test_after_end():
    make_list = LinkedList()
    make_list.insert(3)
    make_list.insert(1)
    make_list.append(5)
    make_list.append(11)
    make_list.append(7)
    make_list.insertAfter(7,8)
    actual = str(make_list)
    expected = "{ 1 } -> { 3 } -> { 5 } -> { 11 } -> { 7 } -> { 8 } -> NULL"
    assert actual == expected

##Challenge 07

def test_greater_than_list_length():
    make_list = LinkedList()
    make_list.append("a")
    make_list.append("b")
    make_list.append("c")
    with pytest.raises(IndexError):
        make_list.k_fromthe_end(4)

def test_same_length_k():
    make_list = LinkedList()
    make_list.append("a")
    make_list.append("b")
    make_list.append("c")
    actual = make_list.k_fromthe_end(2)
    expected = "a"
    assert actual == expected


def test_negative_integer_k():
    make_list = LinkedList()
    make_list.append("a")
    make_list.append("b")
    make_list.append("c")
    with pytest.raises(ValueError):
        make_list.k_fromthe_end(-1)

def test_length_one_k():
    make_list = LinkedList()
    make_list.append("a")
    actual = make_list.k_fromthe_end(0)
    expected = "a"
    assert actual == expected




def test_k_in_middle():
    make_list = LinkedList()
    make_list.append("a")
    make_list.append("b")
    make_list.append("mid")
    make_list.append("d")
    make_list.append("e")
    actual = make_list.k_fromthe_end(2)
    expected = "mid"
    assert actual == expected


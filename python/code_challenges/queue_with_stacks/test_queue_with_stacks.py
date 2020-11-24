import pytest
from queue_with_stacks import Stack, PsuedoQueue, InvalidOperationError



def test_pop_single():
    s = Stack()
    s.push("apple")
    actual = s.pop()
    expected = "apple"
    assert actual == expected


def test_pop_some():
    s = Stack()
    s.push("apple")
    s.push("banana")
    s.push("cucumber")
    s.pop()
    actual = s.pop()
    expected = "banana"
    assert actual == expected


def test_peek():
    s = Stack()
    s.push("apple")
    s.push("banana")
    actual = s.peek()
    expected = "banana"
    assert actual == expected


def test_peek_empty():
    s = Stack()
    with pytest.raises(InvalidOperationError) as e:
        s.peek()

    assert str(e.value) == "Method not allowed on empty collection"


def test_pop_empty():
    s = Stack()
    with pytest.raises(InvalidOperationError) as e:
        s.pop()

    assert str(e.value) == "Method not allowed on empty collection"

def test_empty_PsuedoQueue():
    queue = PsuedoQueue()
    queue.enqueue(1)
    actual = queue.top.value
    expected = 1
    assert actual == expected

def test_multiple_enqueue_into_PsudeoQueue():
    queue = PsuedoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    actual = queue.top.value
    expected = 1
    assert actual == expected


def test_dequeue_fom_PsuedoQueue():
    queue = PsuedoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    actual = queue.dequeue()
    expected = 1
    assert actual == expected


def test_multiple_dequeue_from_PsudeoQueue():
    queue = PsuedoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    queue.dequeue()
    actual = queue.dequeue()
    expected = 3
    assert actual == expected


def test_dequeue_empty_PsuedoQueue():
    queue = PsuedoQueue()
    actual = queue.dequeue()
    expected = None
    assert actual == expected

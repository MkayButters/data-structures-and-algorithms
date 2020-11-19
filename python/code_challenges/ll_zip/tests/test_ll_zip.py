from linked_list.linked_list import LinkedList
from ll_zip.ll_zip import zip_lists
import pytest


def test_happy_zipped_list():
    ll_one = LinkedList(["a", "b", "c"])
    ll_two = LinkedList(["1", "2", "3"])
    zipped = zip_lists(ll_one, ll_two)
    assert zipped.value == "a"

def test_edge_cases():
    ll_one = LinkedList(["a", "b", "c", "d", "q"])
    ll_two = LinkedList(["1", "2", "3"])
    zipped = zip_lists(ll_one, ll_two)
    expected = ["a", "1", "b", "2", "c", "3", "d", "q"]
    while zipped:
        assert zipped.value == expected.pop(0)
        zipped = zipped.next

def test_expect_epic_fail():
    with pytest.raises(TypeError):
        zip_lists("1" , 1)

def test_no_value_ll_zip():
    ll_one = LinkedList([])
    ll_two = LinkedList([])
    actual = zip_lists(ll_one, ll_two)
    expected = None
    assert actual == expected

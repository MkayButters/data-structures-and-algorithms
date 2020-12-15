from merge_sort import merge_sort

def test_length_none():
    arr = []
    actual = merge_sort(arr)
    expected = "no bueno, lista es no provechoso"
    assert actual == expected

def test_length_one():
    arr = [1]
    actual = merge_sort(arr)
    expected = "no bueno, lista es no provechoso"
    assert actual == expected

def test_negative_numbers():
    arr = [1,6,-4,3]
    merge_sort(arr)
    actual = arr
    expected = [-4,1,3,6]
    assert actual == expected

def test_same_numbers():
    arr = [1,1,2,6,3,3,-1,-2]
    merge_sort(arr)
    actual = arr
    expected = [-2,-1,1,1,2,3,3,6]
    assert actual == expected

def test_happy_path():
    arr = [2,1,3,4,6]
    merge_sort(arr)
    actual = arr
    expected = [1,2,3,4,6]
    assert actual == expected

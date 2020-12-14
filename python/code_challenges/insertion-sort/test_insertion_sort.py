from insertion_sort import insertion_sort

def test_empty_array():
    arr = []
    actual = insertion_sort(arr)
    expected = "empty array"
    assert actual == expected

def test_single_array():
    arr = [1]
    actual = insertion_sort(arr)
    expected = "only one number bud"
    assert actual == expected

def test_negative_array():
    arr = [-1, 21, 3, 24, -7, 8]
    actual = insertion_sort(arr)
    expected = [-7,-1,3,8,21,24]
    assert actual == expected

def test_happy_path():
    arr = [2, 4, 6, 3, 5]
    actual = insertion_sort(arr)
    expected = [2,3,4,5,6]
    assert actual == expected

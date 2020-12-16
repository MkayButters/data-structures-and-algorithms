from quick_sort import quick_sort

def test_empty_list():
    arr = []
    low = None
    high = None
    actual = quick_sort(arr, low, high)
    expected = "no bueno, lista es no provechoso"
    assert actual == expected

def test_single_number_list():
    arr = [1]
    low = 0
    high = 0
    quick_sort(arr, low, high)
    actual = arr
    expected = [1]
    assert actual == expected

def test_negative_number_list():
    arr = [1,7,2,-3,11,12,5]
    quick_sort(arr,0,6)
    actual = arr
    expected = [-3,1,2,5,7,11,12]
    assert actual == expected

def test_same_numbers_list():
    arr = [1,1,-1,2,3,7,-1]
    quick_sort(arr,0,6)
    actual = arr
    expected = [-1,-1,1,1,2,3,7]
    assert actual == expected

def test_happy_path():
    arr = [4,3,5,2,7]
    quick_sort(arr,0,4)
    actual = arr
    expected = [2,3,4,5,7]
    assert actual == expected



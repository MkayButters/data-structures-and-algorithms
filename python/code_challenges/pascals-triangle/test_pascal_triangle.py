from pascal_triangle import pascals_triangle

def test_happy_path():
    actual = pascals_triangle(5)
    expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert actual == expected

def test_no_lines():
    actual = pascals_triangle(0)
    expected = []
    assert actual == expected

def test_string_line():
    actual = pascals_triangle('blah')
    expected = "no bueno, lista es no provechoso"
    assert actual == expected

def test_blank_line():
    actual = pascals_triangle()
    expected = []
    assert actual == expected

def test_NAN_line():
    actual = pascals_triangle(1.01)
    expected = 'no bueno, lista es no provechoso'
    assert actual == expected

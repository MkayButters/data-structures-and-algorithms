from multi_bracket_validation import check


def test_happy_path_true():
    string = '[[{{}}]]'
    actual = check(string)
    expected = True
    assert actual == expected

def test_angry_path_false():
    string = '[[{[}'
    actual = check(string)
    expected = False
    assert actual == expected


def test_edge_case1():
    string = '{}[]()(blad)'
    actual = check(string)
    expected = True
    assert actual == expected

def test_false2():
    string = '[([{'
    actual = check(string)
    expected = False
    assert actual == expected

def test_false3():
    string = '[[[[[[[[[[[(){'
    actual = check(string)
    expected = False
    assert actual == expected

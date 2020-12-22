from repeated_word import strip_down, not_split, seen_word, which_word_is_repeated_first


def test_strip_down():
    strip = strip_down('Once upon a time, !there was a brave princess who..')
    actual = strip
    expected = "Once upon a time there was a brave princess who"
    assert actual == expected

def test_strip_down_only():
    strip = strip_down("!@#$")
    actual = strip
    expected = ""
    assert actual == expected

def test_not_split():
    split = not_split("Once upon a time there was a brave princess who")
    actual = split
    expected = ["Once", "upon", "a", "time", "there", "was", "a", "brave", "princess", "who"]
    assert actual == expected

def test_not_split_empty():
    actual = not_split("")
    expected = []
    assert actual == expected


def test_seen_word():
    split = not_split('Once upon a time there was a brave princess who')
    actual = seen_word(split)
    expected = "a"
    assert actual == expected

def test_which_word_is_repeated_first():
    actual = which_word_is_repeated_first("Once upon a time there was a brave princess who")
    expected = 'a'
    assert actual == expected

def test_which_word_is_repeated_first():
    actual = which_word_is_repeated_first("It was the best of times, it was the worst of times, # it was the ag#e of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or @   for evil, in the superlative degree of comparison only..")
    expected = 'it'
    assert actual == expected


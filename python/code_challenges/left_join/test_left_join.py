from left_join import HashTable, left_join

def test_happy_path():
    t1 = HashTable(4)
    t2 = HashTable(3)
    t1.set('happy', 'excited')
    t2.set('happy', 'sad')
    t1.set('mad', 'angry')
    t2.set('mad', 'delighted')
    t1.set('lost', 'failed')
    t2.set('lost', 'won')
    t1.set('shark', 'tornado')
    results = left_join(t1,t2)
    assert ['lost', 'failed', 'won'] in results
    assert ['shark', 'tornado', None] in results
    assert ['happy', 'excited', 'sad'] in results
    assert ['mad', 'angry', 'delighted'] in results


def test_empty_tables():
    t1 = HashTable(0)
    t2 = HashTable(0)
    actual = left_join(t1,t2)
    expected = []
    assert actual == expected

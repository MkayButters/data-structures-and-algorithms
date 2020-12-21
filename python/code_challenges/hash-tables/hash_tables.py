from link_list import LinkedList

class Hashtable:

    def __init__(self, size=1024):
        self._size = size
        self._buckets = size * [None]

    def _hash(self, key):

        sum = 0

        for ch in key:
            sum += ord(ch)

        primed = sum * 19

        index = primed % self._size

        return index


    def set(self, key, value):

        hashed_key_index = self._hash(key)

        if not self._buckets[hashed_key_index]:
            self._buckets[hashed_key_index] = LinkedList()

        self._buckets[hashed_key_index].add((key, value))

    def get(self,requesting_key):

        hashed_key_index = self._hash(requesting_key)
        bucket = self._buckets[hashed_key_index]
        current = bucket.head

        while current:
            pair = current.data
            stored_key = pair[0]
            stored_value = pair[1]
            if stored_key == requesting_key:
                return stored_value

            current = current.next

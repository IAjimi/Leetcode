from collections import defaultdict


class MapSum:
    """
    Runtime: 24 ms, faster than 97.01% of Python3 online submissions.
    Memory Usage: 14.4 MB, less than 26.42% of Python3 online submissions.

    Basic idea: a trie for prefix search and a second dict with the sums.
    Really could be combined into 1, adding '*' for sums, but that is 10ms slower and
    not much better memory-wise.

    Overrides are handled with a small "cheat": a dictionary that stores words
    that have already been inserted. If adding a word that was already there,
    MapSum() computes the change in value (delta) and proceeds with inserting
    the word with that delta.
    """

    def __init__(self):
        self.max_ix = 1  # next unique index available
        self.trie = {0: {}}  # dict of dicts
        self.trie_sum = defaultdict(int)  # dict of values
        self.dictionary = {}  # a cheat for overrides

    def insert(self, key: str, val: int) -> None:
        """
        Dispatch for insert calls.

        If the word was already inserted, it is reinserted with the
        delta in values. Otherwise, proceed with insert with val.
        """
        if key in self.dictionary:
            delta = val - self.dictionary[key]
            self.dictionary[key] = val
            self.realInsert(key, delta)
        else:
            self.dictionary[key] = val
            self.realInsert(key, val)

    def realInsert(self, key: str, val: int) -> None:
        ix = 0

        for letter in key:
            if letter in self.trie[ix]:
                self.trie_sum[ix] += val  # update sum
                ix = self.trie[ix][letter]  # move to next node
            else:
                self.max_ix += 1  # next unique int
                self.trie[ix][letter] = self.max_ix  # create link to next node
                self.trie[self.max_ix] = {}  # create next node with link to empty dict
                self.trie_sum[ix] += val
                ix = self.max_ix

        self.trie_sum[ix] += val  # for end of word

    def sum(self, prefix: str) -> int:
        ix = 0

        for letter in prefix:
            if letter in self.trie[ix]:
                ix = self.trie[ix][letter]  # move to next node
            else:
                return 0

        return self.trie_sum[ix]


def test_insert():
    obj = MapSum()
    obj.insert("apple", 3)
    assert 3 == obj.sum("app")
    obj.insert("app", 2)
    assert 3 + 2 == obj.sum("ap")


def test_override():
    obj = MapSum()
    obj.insert("apple", 5)
    assert 5 == obj.sum("apple")
    obj.insert("apple", 1)
    assert 1 == obj.sum("apple")
    obj.insert("app", 3)
    assert 1 + 3 == obj.sum("app")
    assert 1 == obj.sum("apple")


if __name__ == "__main__":
    test_insert()
    test_override()

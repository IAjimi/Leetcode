class MyHashMap:
    """
    Runtime: 305 ms, faster than 70.57% of Python3 online submissions for Design HashMap.
    Memory Usage: 18.2 MB, less than 29.73% of Python3 online submissions for Design HashMap.
    """

    def __init__(self):
        self.m = 1 + 10**4  # based on max number of operations - can be decreased
        self.p = 10_000_019
        self.values = [[] for _ in range(self.m)]

    def __hash(self, key: int) -> int:
        return (key % self.p) % self.m

    def put(self, key: int, value: int) -> None:
        hash_key = self.__hash(key)
        for i, (k, v) in enumerate(self.values[hash_key]):
            if k == key:
                self.values[hash_key][i] = (key, value)
                return

        self.values[hash_key].append((key, value))

    def get(self, key: int) -> int:
        hash_key = self.__hash(key)
        for k, v in self.values[hash_key]:
            if k == key:
                return v

        return -1

    def remove(self, key: int) -> None:
        hash_key = self.__hash(key)
        for i, (k, v) in enumerate(self.values[hash_key]):
            if k == key:
                self.values[hash_key].pop(i)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

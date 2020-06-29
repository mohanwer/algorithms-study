# https://leetcode.com/problems/design-hashmap/
from collections import defaultdict


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        for i, v in enumerate(self.hashmap):
            if v[0] == key:
                self.hashmap[i] = (key, value)
        self.hashmap.append((key, value))


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        for v in self.hashmap:
            if v[0] == key:
                return v[1]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        for i, v in enumerate(self.hashmap):
            if v[0] == key:
                self.hashmap.pop(i)
                return


hashMap = MyHashMap()
hashMap.put(1, 1)
hashMap.put(2, 2)
hashMap.get(1)
hashMap.get(3)
hashMap.put(2, 1)
hashMap.get(2)
hashMap.remove(2)
hashMap.get(2)

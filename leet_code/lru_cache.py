# https://leetcode.com/problems/lru-cache/
# https://www.geeksforgeeks.org/doubly-linked-list/
from collections import OrderedDict

class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head, self.tail = DLinkedNode(), DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def __add_node(self, node):
        self.size += 1
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def __remove_node(self, node):
        self.size -= 1
        prev = node.prev
        new_node = node.next

        prev.next = new_node
        new_node.prev = prev

    def __move_to_head(self, node):
        self.__remove_node(node)
        self.__add_node(node)

    def __pop_tail(self):
        res = self.tail.prev
        self.__remove_node(res)
        return res

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if node is None:
            return -1
        self.__move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)
        if node is None:
            node = DLinkedNode()
            node.key = key
            node.value = value
            self.cache[key] = node
            self.__add_node(node)
            if self.capacity < self.size:
                res = self.__pop_tail()
                del self.cache[res.key]
        else:
            node.value = value
            self.__move_to_head(node)

class LRUCacheDict:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        v = self.cache.get(key, None)
        if v is None:
            return -1
        self.size += 1
        self.cache.move_to_end(key)
        return v

    def remove(self, key: int) -> int:
        del self.cache[key]
        self.size -= 1

    def put(self, key, value):
        v = self.cache.get(key, None)
        if v is None:
            self.cache[key] = value
            self.size += 1
            if self.size > self.capacity:
                self.cache.popitem(last=False)
        else:
            self.cache[key] = value
        self.cache.move_to_end(key)



g = LRUCache(2)
g.put(1, 1)
g.put(2, 2)
g.get(1)
g.get(2)
g.put(3, 3)
g.get(2)
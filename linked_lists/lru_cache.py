class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.value = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int) -> None:
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.keys = {}
        self.capacity = capacity
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key) -> int:
        node = self.keys[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key, value):
        if key in self.keys:
            old_node = self.keys[key]
            self.remove(old_node)
        node = Node(key, value)
        self.add(node)
        self.keys[key] = node
        if len(self.keys) > self.capacity:
            node_to_remove = self.head.next
            self.remove(node_to_remove)
            del self.keys[node_to_remove.key]

    def add(self, node: Node) -> None:
        tail_prev = self.tail.prev
        tail_prev.next = node
        node.prev = tail_prev
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node: Node) -> None:
        node_prev, node_next = node.prev, node.next
        node_prev.next, node_next.prev = node_next, node_prev

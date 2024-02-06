from typing import Optional


class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_front(self, val) -> None:
        node = Node(val)
        self.size += 1
        if self.head.next == self.tail:
            self.head.next = node
            node.prev = self.head
            node.next = self.tail
            self.tail.prev = node
            return
        head_next = self.head.next
        self.head.next = node
        node.next = head_next
        node.prev = self.head
        head_next.prev = node

    def add_to_tail(self, val) -> None:
        self.size += 1
        node = Node(val)
        prev = self.tail.prev
        prev.next = node
        node.next = self.tail
        node.prev = prev
        self.tail.prev = node

    def pop_head(self) -> Optional[int]:
        if self.size == 0:
            return None
        self.size -= 1
        node = self.head.next
        self.remove(node)
        return node.val

    def pop_tail(self) -> Optional[int]:
        if self.size == 0:
            return None
        self.size -= 1
        node = self.tail.prev
        self.remove(node)
        return node.val

    def remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def peak_head(self) -> Optional[int]:
        if self.size == 0:
            return None
        return self.head.next.val

    def peak_tail(self) -> Optional[int]:
        if self.size == 0:
            return None
        return self.tail.prev.val


q = DoubleLinkedList()
front_queue = [1, 2, 3, 4]
back_queue = [5, 6, 7, 8]
for f in front_queue:
    q.add_to_front(f)
for b in back_queue:
    q.add_to_tail(b)
while front_queue:
    v = front_queue.pop()
    assert v == q.pop_head()
while back_queue:
    v = back_queue.pop()
    assert v == q.pop_tail()

assert q.size == 0

q.add_to_front(1)
q.add_to_front(2)
q.add_to_front(3)
assert q.peak_head() == 3
assert q.peak_tail() == 1
q.add_to_tail(7)
assert q.peak_tail() == 7
assert q.pop_head() == 3
assert q.pop_tail() == 7
assert q.pop_tail() == 1
assert q.pop_tail() == 2
assert not q.peak_head()
assert not q.size

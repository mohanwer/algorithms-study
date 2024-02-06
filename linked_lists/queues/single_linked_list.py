from typing import Optional


class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None


class SingleLinkedList:
    def __init__(self) -> None:
        self.head, self.tail = None, None

    def add(self, val: int) -> None:
        node = Node(val)
        if not self.tail:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def pop_head(self) -> Optional[Node]:
        if not self.head:
            return None
        node = self.head

        self.head = self.head.next
        if self.tail == node:
            self.tail = self.tail.next

        return node.val


q = SingleLinkedList()
q.add(1)
q.add(2)
assert q.pop_head() == 1
assert q.pop_head() == 2
assert not q.tail

q.add(1)
q.add(3)
assert q.tail.val == 3

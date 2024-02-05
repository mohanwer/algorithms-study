class LinkedList:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None

    def tostring(self):
        return self.val

def build_linked_list(size: int) -> LinkedList:
    node, prev = None, None
    for i in range(size, 0, -1):
        node = LinkedList(i)
        if prev:
            node.next = prev
        prev = node
    return node

even_sized_ll = build_linked_list(4)
odd_sized_ll = build_linked_list(5)

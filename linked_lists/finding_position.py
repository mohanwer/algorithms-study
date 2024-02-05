from utils import LinkedList, even_sized_ll, odd_sized_ll

def n_node(node: LinkedList, n:int) -> LinkedList:
    dummy = node
    for _ in range(n - 1):
        dummy = dummy.next
    return dummy

def n_after(node: LinkedList, n: int) -> LinkedList:
    dummy = node
    for _ in range(n):
        dummy = dummy.next
    return dummy

def n_from_end(node: LinkedList, n: int) -> LinkedList:
    fast = node
    for _ in range(n):
        fast = fast.next
    
    if not fast:
        return node.next
    
    slow = node
    while fast.next:
        fast = fast.next
        slow = slow.next

    return slow

def middle(node: LinkedList) -> LinkedList:
    fast, slow = node, node
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    return slow


res = n_after(odd_sized_ll, 2)
assert res.val == 3

res = n_from_end(odd_sized_ll, 2)
assert res.val == 3

res = middle(odd_sized_ll)
assert res.val == 3

res = middle(even_sized_ll)
assert res.val == 2
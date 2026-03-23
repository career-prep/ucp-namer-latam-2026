# Data Structure Implementation: Doubly Linked List
# time complexity per method noted inline
# 20 minutes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def insertAtFront(head, val):  # O(1)
    new_node = Node(val)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node

def insertAtBack(head, tail, val):  # O(1)
    new_node = Node(val)
    if not tail:
        return new_node, new_node
    tail.next = new_node
    new_node.prev = tail
    return head, new_node

def insertAfter(head, val, loc):  # O(1)
    new_node = Node(val)
    new_node.next = loc.next
    new_node.prev = loc
    if loc.next:
        loc.next.prev = new_node
    loc.next = new_node
    return head

def insertBefore(head, val, loc):  # O(1)
    new_node = Node(val)
    new_node.next = loc
    new_node.prev = loc.prev
    if loc.prev:
        loc.prev.next = new_node
    else:
        head = new_node
    loc.prev = new_node
    return head

def deleteFront(head):  # O(1)
    if not head:
        return None
    head = head.next
    if head:
        head.prev = None
    return head

def deleteBack(head, tail):  # O(1)
    if not tail:
        return None, None
    if not tail.prev:
        return None, None
    tail = tail.prev
    tail.next = None
    return head, tail

def deleteNode(head, loc):  # O(1)
    if loc.prev:
        loc.prev.next = loc.next
    else:
        head = loc.next
    if loc.next:
        loc.next.prev = loc.prev
    return head

def length(head):  # O(n)
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next
    return count

def reverseIterative(head):  # O(n)
    curr = head
    new_head = None
    while curr:
        curr.prev, curr.next = curr.next, curr.prev
        new_head = curr
        curr = curr.prev  # curr.prev is now what was next
    return new_head

def reverseRecursive(head):  # O(n)
    def helper(node):
        if not node:
            return None
        node.prev, node.next = node.next, node.prev
        if not node.prev:  # node.prev is now what was next; None means we're at the new head
            return node
        return helper(node.prev)
    return helper(head)

# helpers for testing
def to_list(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    return result

def from_list(lst):
    if not lst:
        return None, None
    head = Node(lst[0])
    tail = head
    for val in lst[1:]:
        head, tail = insertAtBack(head, tail, val)
    return head, tail

# test cases
head, tail = from_list([1, 2, 3, 4, 5])
assert to_list(head) == [1, 2, 3, 4, 5]

head = insertAtFront(head, 0)
assert to_list(head) == [0, 1, 2, 3, 4, 5]

head, tail = insertAtBack(head, tail, 6)
assert to_list(head) == [0, 1, 2, 3, 4, 5, 6]

curr = head
while curr.data != 3:
    curr = curr.next
head = insertAfter(head, 99, curr)
assert to_list(head) == [0, 1, 2, 3, 99, 4, 5, 6]

curr = head
while curr.data != 3:
    curr = curr.next
head = insertBefore(head, 88, curr)
assert to_list(head) == [0, 1, 2, 88, 3, 99, 4, 5, 6]

head = deleteFront(head)
assert to_list(head) == [1, 2, 88, 3, 99, 4, 5, 6]

head, tail = deleteBack(head, tail)
assert to_list(head) == [1, 2, 88, 3, 99, 4, 5]

curr = head
while curr.data != 99:
    curr = curr.next
head = deleteNode(head, curr)
assert to_list(head) == [1, 2, 88, 3, 4, 5]

assert length(head) == 6

head = reverseIterative(head)
assert to_list(head) == [5, 4, 3, 88, 2, 1]

head = reverseRecursive(head)
assert to_list(head) == [1, 2, 88, 3, 4, 5]

print("yay!!")

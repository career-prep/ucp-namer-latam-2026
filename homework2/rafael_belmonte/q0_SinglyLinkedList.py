# Data Structure Implementation: Singly Linked List
# time complexity per method noted inline
# 35 minutes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtFront(head, val):  # O(1)
    new_node = Node(val)
    new_node.next = head
    return new_node

def insertAtBack(head, val):  # O(n)
    new_node = Node(val)
    if not head:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    return head

def insertAfter(head, val, loc):  # O(1)
    new_node = Node(val)
    new_node.next = loc.next
    loc.next = new_node
    return head

def insertBefore(head, val, loc):  # O(n)
    new_node = Node(val)
    if head == loc:
        new_node.next = head
        return new_node
    curr = head
    while curr.next and curr.next != loc:
        curr = curr.next
    new_node.next = loc
    curr.next = new_node
    return head

def deleteFront(head):  # O(1)
    if not head:
        return None
    return head.next

def deleteBack(head):  # O(n)
    if not head or not head.next:
        return None
    curr = head
    while curr.next.next:
        curr = curr.next
    curr.next = None
    return head

def deleteNode(head, loc):  # O(n)
    if not head:
        return None
    if head == loc:
        return head.next
    curr = head
    while curr.next and curr.next != loc:
        curr = curr.next
    if curr.next:
        curr.next = loc.next
    return head

def length(head):  # O(n)
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next
    return count

def reverseIterative(head):  # O(n)
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def reverseRecursive(head):  # O(n)
    def helper(curr, prev):
        if not curr:
            return prev
        next_node = curr.next
        curr.next = prev
        return helper(next_node, curr)
    return helper(head, None)

# helpers for testing
def to_list(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    return result

def from_list(lst):
    head = None
    for val in reversed(lst):
        head = insertAtFront(head, val)
    return head

# test cases
head = from_list([1, 2, 3, 4, 5])
assert to_list(head) == [1, 2, 3, 4, 5]

head = insertAtFront(head, 0)
assert to_list(head) == [0, 1, 2, 3, 4, 5]

head = insertAtBack(head, 6)
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

head = deleteBack(head)
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

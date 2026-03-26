# Question 2: Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def insertAtFront(head, val):
    # Time and Space: O(1)
    new_node = Node(val)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node


def insertAtBack(head, tail, val):
    # Time and Space: O(1)
    new_node = Node(val)
    if not head:
        return new_node
    new_node.prev = tail
    tail.next = new_node
    return head


def insertAfter(head, val, loc):
    # Time and Space: O(1)
    new_node = Node(val)
    new_node.next = loc.next
    new_node.prev = loc
    if loc.next:
        loc.next.prev = new_node
    loc.next = new_node
    return head


def insertBefore(head, val, loc):
    # Time and Space: O(1)
    new_node = Node(val)
    new_node.next = loc
    new_node.prev = loc.prev
    if loc.prev:
        loc.prev.next = new_node
    else:
        head = new_node
    loc.prev = new_node
    return head


def deleteFront(head):
    # Time and Space: O(1)
    if not head:
        return None
    new_head = head.next
    if new_head:
        new_head.prev = None
    return new_head


def deleteBack(head, tail):
    # Time and Space: O(1)
    if not head or head == tail:
        return None
    new_tail = tail.prev
    new_tail.next = None
    return head


def deleteNode(head, loc):
    # Time and Space: O(1)
    if loc.prev:
        loc.prev.next = loc.next
    else:
        head = loc.next
    if loc.next:
        loc.next.prev = loc.prev
    return head


def length(head):
    # Time: O(n) and Space: O(1)
    count = 0
    while head:
        count += 1
        head = head.next
    return count


def reverseIterative(head):
    # Time: O(n) and Space: O(1)
    current = head
    new_head = None
    while current:
        current.prev, current.next = current.next, current.prev
        new_head = current
        current = current.prev
    return new_head


def reverseRecursive(head):
    # Time: O(n) and Space: O(n) — recursion stack depth is n
    def helper(node):
        if not node:
            return None
        node.prev, node.next = node.next, node.prev
        if not node.prev:
            return node
        return helper(node.prev)

    return helper(head)

# time: 20 minutes

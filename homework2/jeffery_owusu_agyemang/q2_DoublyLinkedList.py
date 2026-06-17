class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# O(1)
def insertAtFront(head, val):
    new_node = Node(val)
    if head:
        head.prev = new_node
        new_node.next = head
    return new_node

# O(1) (assuming tail is provided)
def insertAtBack(head, tail, val):
    new_node = Node(val)
    if not head:
        return new_node, new_node
    tail.next = new_node
    new_node.prev = tail
    return head, new_node

# O(1)
def insertAfter(head, val, loc):
    if not loc:
        return head
    new_node = Node(val)
    new_node.next = loc.next
    new_node.prev = loc
    if loc.next:
        loc.next.prev = new_node
    loc.next = new_node
    return head

# O(1)
def insertBefore(head, val, loc):
    if not loc:
        return head
    new_node = Node(val)
    new_node.next = loc
    new_node.prev = loc.prev
    if loc.prev:
        loc.prev.next = new_node
    else:
        head = new_node
    loc.prev = new_node
    return head

# O(1)
def deleteFront(head):
    if not head:
        return None
    if not head.next:
        return None
    head = head.next
    head.prev = None
    return head

# O(1)
def deleteBack(head, tail):
    if not tail:
        return None, None

    if not tail.prev:
        return None, None
    tail = tail.prev
    tail.next = None
    return head, tail

# O(1)
def deleteNode(head, loc):
    if not loc:
        return head
    if loc.prev:
        loc.prev.next = loc.next
    else:
        head = loc.next  # deleting head
    if loc.next:
        loc.next.prev = loc.prev
    return head

# O(n)
def length(head):
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next
    return count

# O(n)
def reverseIterative(head):
    curr = head
    prev = None
    while curr:
        curr.prev, curr.next = curr.next, curr.prev
        prev = curr
        curr = curr.prev
    return prev

# O(n)
def reverseRecursive(head):
    if not head:
        return None
    def helper(node):
        if not node:
            return None
        node.prev, node.next = node.next, node.prev
        if not node.prev:
            return node
        return helper(node.prev)
    return helper(head)
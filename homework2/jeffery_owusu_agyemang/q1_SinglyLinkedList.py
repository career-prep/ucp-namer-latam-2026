class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# O(1)
def insertAtFront(head, val):
    new_node = Node(val)
    new_node.next = head
    return new_node

# O(n)
def insertAtBack(head, val):
    new_node = Node(val)
    if not head:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    return head

# O(1)
def insertAfter(head, val, loc):
    if not loc:
        return head
    new_node = Node(val)
    new_node.next = loc.next
    loc.next = new_node
    return head

# O(n)
def insertBefore(head, val, loc):
    if not head or not loc:
        return head
    if head == loc:
        return insertAtFront(head, val)
    prev = None
    curr = head
    while curr and curr != loc:
        prev = curr
        curr = curr.next
    if curr == loc:
        new_node = Node(val)
        prev.next = new_node
        new_node.next = curr
    return head

# O(1)
def deleteFront(head):
    if not head:
        return None
    return head.next

# O(n)
def deleteBack(head):
    if not head or not head.next:
        return None
    curr = head
    while curr.next.next:
        curr = curr.next
    curr.next = None
    return head

# O(n)
def deleteNode(head, loc):
    if not head or not loc:
        return head
    if head == loc:
        return head.next
    prev = None
    curr = head
    while curr and curr != loc:
        prev = curr
        curr = curr.next
    if curr == loc:
        prev.next = curr.next
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
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

# O(n)
def reverseRecursive(head):
    def helper(node, prev):
        if not node:
            return prev
        nxt = node.next
        node.next = prev
        return helper(nxt, node)
    return helper(head, None)
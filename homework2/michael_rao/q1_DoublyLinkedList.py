class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

def insertAtFront(head, val):
    new = Node(val, head, None)
    if head:
        head.prev = new
    return new
# time: O(1)

def insertAtBack(head, val):
    if not head:
        return Node(val)
    curr = head
    while curr.next != None:
        curr = curr.next
    new = Node(val, None, curr)
    curr.next = new
    return head
# time: O(n)

def insertAfter(head, val, loc):
    if not head:
        return Node(val)
    curr = head
    while curr.next != None and curr != loc:
        curr = curr.next
    nxt = curr.next
    new = Node(val, nxt, curr)
    curr.next = new
    if nxt:
        nxt.prev = new
    return head
# time: O(n)

def insertBefore(head, val, loc):
    if not head:
        return Node(val)
    if head == loc:
        new = Node(val, head, None)
        head.prev = new
        return new
    curr = head
    while curr.next != None and curr.next != loc:
        curr = curr.next
    new = Node(val, loc, curr)
    curr.next = new
    loc.prev = new
    return head
# time: O(n)

def deleteFront(head):
    if not head:
        return
    new_head = head.next
    if new_head:
        new_head.prev = None
    return new_head
# time: O(1)

def deleteBack(head):
    if not head or not head.next:
        return
    curr = head
    while curr.next != None:
        prev = curr
        curr = curr.next
    prev.next = None
    return head
# time: O(n)

def length(head):
    if not head:
        return 0
    count = 0
    curr = head
    while curr != None:
        curr = curr.next
        count += 1
    return count
# time: O(n)

def reverseIterative(head):
    if not head:
        return head
    curr = head
    new_head = None
    while curr != None:
        nxt = curr.next
        curr.next = curr.prev
        curr.prev = nxt
        new_head = curr
        curr = nxt
    return new_head
# time: O(n)

def reverseRecursive(head):
    if not head or not head.next:
        if head:
            head.prev = None
        return head
    new_head = reverseRecursive(head.next)
    head.next.next = head
    head.prev = head.next
    head.next = None
    return new_head
# time: O(n)

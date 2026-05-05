class Node:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next

def insertAtFront(head, val):
    return Node(val, head)
# time: O(1)

def insertAtBack(head, val):
    if not head:
        return Node(val)
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = Node(val)
    return head
# time: O(n)

def insertAfter(head, val, loc):
    if not head:
        return Node(val)
    curr = head
    while curr.next != None and curr != loc:
        curr = curr.next
    curr.next = Node(val, curr.next)
    return head
# time: O(n)

def insertBefore(head, val, loc):
    if not head:
        return Node(val)
    if head == loc:
        return Node(val, head)
    curr = head
    while curr.next != None and curr.next != loc:
        curr = curr.next
    curr.next = Node(val, curr.next)
    return head
# time: O(n)

def deleteFront(head):
    if not head:
        return
    new_head = head.next
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
    if not head or not head.next:
        return head
    prev = None
    curr = head
    while curr != None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
# time: O(n)

def reverseRecursive(head):
    if not head or not head.next:
        return head
    new_head = reverseRecursive(head.next)
    head.next.next = head
    head.next = None
    return new_head
# time: O(n)

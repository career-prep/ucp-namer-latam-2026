#Singly Linked List Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtFront(head, val): #O(1)
    newNode = Node(val)
    newNode.next = head
    return newNode

def insertAtBack(head, val): #O(n)
    newNode = Node(val)
    if not head:
        return newNode
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = newNode
    return head
    
def insertAfter(head, val, loc): #for O(1) time assume that loc exists in the list
    newNode = Node(val)
    if not head:
        return newNode
    newNode.next = loc.next
    loc.next = newNode
    return head
    
def insertBefore(head, val, loc): #O(n) also assuming loc exists
    if not head:
        return Node(val)
    if loc is head:
        return insertAtFront(head, val)
    newNode = Node(val)
    curr = head
    while curr.next != loc:
        curr = curr.next
    curr.next = newNode
    newNode.next = loc
    return head

def deleteFront(head): #O(1)
    if not head or not head.next:
        return None
    head = head.next
    return head

def deleteBack(head): #O(n)
    if not head or not head.next:
        return None
    curr = head
    while curr.next.next:
        curr = curr.next
    curr.next = None
    return head
    
def deleteNode(head, loc): #O(n)
    if not head:
        return head
    if loc == head:
        return deleteFront(head)
    
    curr = head
    while curr.next:
        if curr.next == loc:
            curr.next = loc.next
            loc.next = None
            return head
        curr = curr.next
    return head

def length(head): #O(n)
    if not head:
        return 0
    count = 0
    curr = head
    while curr:
        curr = curr.next
        count += 1
    return count

def reverseIterative(head): #O(n)
    if not head:
        return head
    prev = None
    curr = head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev

def reverseRecursive(head):
    def helper(prev,curr):
        if not curr:
            return prev
        next = curr.next
        curr.next = prev
        return helper(curr, next)
    return helper(None, head)





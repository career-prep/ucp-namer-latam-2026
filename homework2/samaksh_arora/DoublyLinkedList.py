#Doubly Linked List Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def insertAtFront(head, val): #O(1)
    newNode = Node(val)
    if not head:
        return newNode
    newNode.next = head
    head.prev = newNode
    return newNode

def insertAtBack(head, val): #O(n)
    newNode = Node(val)
    if not head:
        return newNode
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = newNode
    newNode.prev = curr
    return head
    
def insertAfter(head, val, loc): #for O(1) time assume that loc exists in the list
    newNode = Node(val)
    if not head:
        return newNode
    newNode.next = loc.next
    newNode.prev = loc
    if loc.next:
        loc.next.prev = newNode

    loc.next = newNode
    return head
    
def insertBefore(head, val, loc): #O(1) assuming loc exists
    if not head:
        return Node(val)
    if loc is head:
        return insertAtFront(head,val) 
    newNode = Node(val)
    newNode.prev = loc.prev
    loc.prev.next = newNode
    newNode.next = loc
    loc.prev = newNode
    return head

def deleteFront(head): #O(1)
    if not head or not head.next:
        return None
    head = head.next
    head.prev = None
    return head

def deleteBack(head,tail): #O(1)
    if not head or head == tail:
        return None

    tail = tail.prev
    tail.next.prev = None
    tail.next = None
    return head
    
def deleteNode(head, loc): #O(1)
    if not head:
        return head
    if loc is head:
        return deleteFront(head)
    if loc.next is None:
        return deleteBack(head, loc)
    loc.prev.next = loc.next
    loc.next.prev = loc.prev
    loc.next = None
    loc.prev = None
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
    if not head or not head.next:
        return head
    prev = None
    curr = head
    while curr:
        curr.next, curr.prev  = curr.prev, curr.next
        prev = curr
        curr = curr.prev
    return prev

def reverseRecursive(head): #O(n)
    if not head:
        return head
    head.prev, head.next = head.next, head.prev
    if not head.prev:         
        return head            
    return reverseRecursive(head.prev) 





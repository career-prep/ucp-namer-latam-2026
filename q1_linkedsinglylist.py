# 40 minutes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtFront(head, val):
    newNode = Node(val)
    newNode.next = head
    return newNode
    ## creates new Node with data val at front; returns head. O(1) time.

def insertAtBack(head, val):
    newNode = Node(val)
    if head is None:
        return newNode
    
    current = head
    while current.next is not None:
        current = current.next
    current.next = newNode

    return head
    ## creates new Node with data val at end; returns head. O(n) time.

def insertAfter(head, val, loc):
    newNode = Node(val)

    if head is None:
        return newNode
    
    current = head
    while current.next is not None:
        current = current.next
    current.next = newNode
    return head
    ## creates new Node with data val after Node loc; returns head. O(1) time.

def insertBefore(head, val, loc):
    if head is None:
        head = Node(val)
        return head

    if head is loc:
        new_head = Node(val)
        new_head.next = head
        return new_head
    
    prev = head
    current = head.next
    while current.next is not None and current is not loc:
        prev = current
        current = current.next
    
    newNode = Node(val)
    newNode.next = current
    prev.next = newNode
    return head
    ## creates new Node with data val before Node loc; returns head. O(n) time.

def deleteFront(head):
    if head is None:
        return None
    head = head.next
    return head
    ## removes first Node; returns head. O(1) time.

def deleteBack(head):
    if head is None:
        return None

    prev = head
    current = head.next
    while current is not None:
        prev = current
        current = current.next
    prev.next = None
    return head

    ## removes last Node; returns head. O(n) time.

def deleteNode(head, loc):
    if head is None or loc is None:
        return None
    
    if head is loc:
        return head.next

    prev = head
    current = head.next
    while current is not loc and current is not None:
        prev = current
        current = current.next

    if current is None:
        return head

    prev.next = current.next

    return head
    ## deletes Node loc; returns head. O(n) time.

def length(head):
    n = 0 
    current = head
    while current is not None:
        n+=1
        current = current.next
    return n
    ## returns length of the list. O(n) time.

def reverseIterative(head):
    prev = None
    current = head
    while current is not None:
        nexttemp = current.next
        current.next = prev
        prev = current
        current = nexttemp
    return prev
    ## reverses the linked list iteratively. O(n) time.

def reverseRecursive(head):
    return helperfunction(head, None)
    ## reverses the linked list recursively (Hint: you will need a helper function.) O(n) time.

def helperfunction(current, prev):
    if current is None:
        return prev
    nexttemp = current.next
    current.next = prev
    return helperfunction(nexttemp,current)
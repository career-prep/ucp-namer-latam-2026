# Time Spent: 20 minutes

from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None

# Creates new Node with data val at front; returns head, O(1) time.
def insertAtFront(head: Node, val: int) -> Node: 
    new_node = Node(val)
    new_node.next = head

    if head:
        head.prev = new_node

    new_node.prev = None

    return new_node

# Creates new Node with data val at end; returns head, O(1) time.
def insertAtBack(head: Node, tail: Node, val: int) -> Node:
    new_node = Node(val)
    
    if not head:
        head = new_node
        tail = new_node
        return head
    
    tail.next = new_node
    new_node.prev = tail

    return head

# Creates new Node with data val after Node loc; returns head, O(1) time.

def insertAfter(head: Node, val: int, loc: Node) -> Node:
    new_node = Node(val)
    new_node.next = loc.next
    new_node.prev = loc

    loc.next = new_node
    return head

# Creates new Node with data val before Node loc; returns head, O(1) time.
def insertBefore(head: Node, val: int, loc: Node) -> Node:
    new_node = Node(val)

    if not head:
        return head
    
    if loc == head:
        new_node.next = head
        head.prev = new_node
        new_node.prev = None
        return new_node

    new_node.next = loc
    new_node.prev = loc.prev
    loc.prev = new_node

    return head

# Removes first Node; returns head, O(1) time.

def deleteFront(head: Optional[Node]) -> Optional[Node]:
    if not head:
        return None
    
    head = head.next
    if head:
        head.prev = None

    return head

# Removes last Node; returns head, O(1) time.

def deleteBack(head: Optional[Node], tail: Optional[Node]) -> Optional[Node]:
    if not head or not tail:
        return None
    
    if head == tail:
        return None
    
    tail.prev.next = None
    tail.prev = None

    return head

# Deletes Node loc; returns head, O(1) time.

def deleteNode(head: Optional[Node], loc: Optional[Node]) -> Optional[Node]:
    if not head or not loc:
        return head
    
    if loc == head:
        head = head.next
        if head:
            head.prev = None
        loc.next = None
        
        return head
    
    if loc.prev:
        loc.prev.next = loc.next
    
    if loc.next:
        loc.next.prev = loc.prev

        loc.next = None
        loc.prev = None

    return head

# Returns length of the list. O(n) time.

def length(head: Optional[Node]) -> int:
    listLength = 0
    
    curr = head
    while curr:
        listLength += 1
        curr = curr.next
    
    return listLength

# Reverses the linked list iteratively. O(n) time.

def reverseIterative(head: Optional[Node]) -> Optional[Node]:
    prev, curr = None, head

    while curr:
        temp = curr.next
        curr.next = curr.prev
        curr.prev = temp
        prev = curr
        curr = temp
    return prev

# Reverses the linked list recursively (Hint: you will need a helper function.) O(n) time.

def reverseRecursive(head: Optional[Node]) -> Optional[Node]:
    return reverseHelper(head, None)

def reverseHelper(curr: Optional[Node], prev: Optional[Node]) -> Optional[Node]:
    if not curr:
        return prev
    
    temp = curr.next
    curr.next = curr.prev
    curr.prev = temp

    return reverseHelper(temp, curr)
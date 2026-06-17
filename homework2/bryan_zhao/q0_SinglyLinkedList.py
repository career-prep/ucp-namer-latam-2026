# Time Spent: 40 minutes

from typing import Optional
class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional[Node] = None

# Creates new Node with data val at front; returns head, O(1) time.
def insertAtFront(head: Node, val: int) -> Node: 
    new_node = Node(val)
    new_node.next = head

    return new_node

# Creates new Node with data val at end; returns head, O(n) time.
def insertAtBack(head: Node, val: int) -> Node:
    new_node = Node(val)
    
    if not head:
        head = new_node
        return head

    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node

    return head

# Creates new Node with data val after Node loc; returns head, O(1) time.

def insertAfter(head: Node, val: int, loc: Node) -> Node:
    new_node = Node(val)
    new_node.next = loc.next
    loc.next = new_node

    return head

# Creates new Node with data val before Node loc; returns head, O(n) time.
def insertBefore(head: Node, val: int, loc: Node) -> Node:
    new_node = Node(val)

    if not head:
        return head
    
    if loc == head:
        new_node.next = head
        return new_node

    curr = head
    while curr.next and curr.next != loc:
        curr = curr.next
    
    if curr.next == loc:
        new_node.next = loc
        curr.next = new_node

    return head

# Removes first Node; returns head, O(1) time.

def deleteFront(head: Optional[Node]) -> Optional[Node]:
    if not head:
        return None
    
    head = head.next
    
    return head

# Removes last Node; returns head, O(n) time.

def deleteBack(head: Optional[Node]) -> Optional[Node]:
    if not head or not head.next:
        return None
    
    curr = head
    while curr.next.next:
        curr = curr.next
    curr.next = None

    return head

# Deletes Node loc; returns head, O(n) time.

def deleteNode(head: Optional[Node], loc: Optional[Node]) -> Optional[Node]:
    if not head:
        return None
    
    if not loc: 
        return head
    
    if loc == head:
        head = head.next
        loc.next = None
        return head
    
    curr = head
    while curr.next and curr.next != loc:
        curr = curr.next
    
    if curr.next == loc:
        curr.next = loc.next
        loc.next = None
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
        curr.next = prev
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
    curr.next = prev

    return reverseHelper(temp, curr)
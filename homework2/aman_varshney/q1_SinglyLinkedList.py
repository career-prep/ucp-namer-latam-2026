# spent 40 minutes

class Node:
    """Node struct in python"""
    def __init__(self, data: int, next: Node = None) -> None:
        self.data = data
        self.next = next 
        
        

def insertAtFront(head, val):
    """Creates a new node with `val` data and links it at the head of the list. O(1) """
    return Node(val, head)
    
    
def insertAtBack(head, val):
    """Creates a new node with `val` data and links it at the end of the list. O(n)"""
    if not head: # empty case
        return Node(val, None) 
    new_node = Node(val, None)
    curr = head
    # traverse to end
    while curr.next:
        curr = curr.next
    # link
    curr.next = new_node
    return head


def insertAfter(head, val, loc):
    """Creates a new node with `val` data after Node `loc` and then returns the head. O(1)"""
    # create new node
    new_node = Node(val, None)
    # link
    temp = loc.next
    new_node.next = temp
    loc.next = new_node
    return head


def insertBefore(head, val, loc):
    """Creates a new node with `val` data before `loc` and then returns the head. O(n)"""
    # check head case
    if (loc == head):
        return Node(val, loc)
    
    # find the node before loc    
    curr = head
    while (curr.next and curr.next != loc):
        curr = curr.next
    if not curr.next: # loc not found
        return None
        
    # create node
    new_node = Node(val, None)
    # link
    curr.next = new_node 
    new_node.next = loc
    return head
    
    
def deleteFront(head):
    """Removes the first node and returns the new head. O(1)"""
    if not head:
        return None
    return head.next


def deleteBack(head):
    """Removes the last node and returns head. O(n)"""
    if not head: # empty case
        return None
    if not head.next:
        return None
    # iterate to the 2nd to last node
    curr = head
    while curr.next.next:
        curr = curr.next
        
    # unlink last node
    curr.next = None
    return head


def deleteNode(head, loc):
    """deletes the node `loc` and returns head. O(n)"""
    if not head: # empty case
        return None
    if (loc == head): # head case
        return loc.next
    
    # find the node before loc
    curr = head
    while (curr.next and curr.next != loc):
        curr = curr.next
    if not curr.next: # loc not found
        return None
    
    # unlink loc
    curr.next = loc.next 
    return head


def length(head) -> int:
    """Returns length of linked list. O(n)"""
    counter = 0
    curr = head
    while curr:
        curr = curr.next
        counter += 1
    return counter


def reverseIterative(head):
    """reverses the linked list iteratively. O(n)"""
    prev = None
    curr = head 

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        
    head = prev 
    return head
    
    
def reverseRecursive(head):
    """Reverses the linked list recursively with a helper. O(n)"""
    # empty + base case
    if not head or not head.next:
        return head
    
    # go to end and unravel
    new_head = reverseRecursive(head.next) 
    # reverse pointer
    head.next.next = head
    head.next = None
    
    return new_head



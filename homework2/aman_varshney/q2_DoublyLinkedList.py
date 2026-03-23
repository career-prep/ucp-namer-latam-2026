# spent 40 minutes

class Node:
    """Node struct in python"""
    def __init__(self, data: int, next: Node = None, prev: Node = None) -> None:
        self.data = data
        self.next = next 
        self.prev = prev
        
        

def insertAtFront(head, val):
    """Creates a new node with `val` data and links it at the head of the list. O(1) """
    if not head:
        return Node(val, None, None)
    new_node = Node(val, head, None)
    head.prev = new_node
    return new_node
    
    
def insertAtBack(head, val):
    """Creates a new node with `val` data and links it at the end of the list. O(n)"""
    if not head: # empty case
        return Node(val, None, None) 
    
    curr = head
    # traverse to end
    while curr.next:
        curr = curr.next
    # link
    new_node = Node(val, None, curr)
    curr.next = new_node
    return head


def insertAfter(head, val, loc):
    """Creates a new node with `val` data after Node `loc` and then returns the head. O(1)"""
    if not head or not loc: # empty case
        return None
    # create new node
    new_node = Node(val, None, None)
    # link
    after_loc = loc.next
    loc.next = new_node
    new_node.next = after_loc
    if after_loc:
        after_loc.prev = new_node
    new_node.prev = loc
    return head


def insertBefore(head, val, loc):
    """Creates a new node with `val` data before `loc` and then returns the head. O(1)"""
    if not head or not loc: # empty case
        return None
    # check head case
    if (loc == head):
        new_node = Node(val, None, None)
        loc.prev = new_node
        new_node.next = loc
        return new_node
    
    # create new node
    new_node = Node(val, None, None)
    # link
    before_loc = loc.prev # stores the node before loc
    loc.prev = new_node
    before_loc.next = new_node
    new_node.next = loc
    new_node.prev = before_loc
    return head
    
    
def deleteFront(head):
    """Removes the first node and returns the new head. O(1)"""
    if not head: # empty case
        return None
    if not head.next: # one element case
        return None
    
    head.next.prev = None
    return head.next


def deleteBack(head, tail):
    """Removes the last node and returns head. O(1)"""
    if not head or not tail: # empty case
        return None
    if head == tail: # only one element
        return None
    
    before_tail = tail.prev
    tail.prev = None
    before_tail.next = None
    return head
    

def deleteNode(head, loc):
    """deletes the node `loc` and returns head. O(1)"""
    if not head or not loc: # empty case
        return None
    if (head == loc): # head case
        return deleteFront(head)
    
    if loc.next:
        loc.next.prev = loc.prev
    if loc.prev:
        loc.prev.next = loc.next
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
    # None <-- 10 <--> 20 <--> 30 --> None  ----  None <-- 30 <--> 20 <--> 10 --> None
    if not head: # empty case
        return None
    
    prev = None
    curr = head 
    while curr:
        next_node = curr.next
        curr.next = prev
        curr.prev = next_node
        prev = curr
        curr = next_node
        
    head = prev 
    return head
    
    
def reverseRecursive(head):
    """Reverses the linked list recursively with a helper. O(n)"""
    # empty + base case
    if not head or not head.next:
        return head
    
    
    # helper
    def recursiveHelper(node): 
        if not node:
            return None
        
        temp = node.next
        node.next = node.prev
        node.prev = temp
        
        if not node.prev:
            return node
        return recursiveHelper(node.prev)
    
    
    return recursiveHelper(head)



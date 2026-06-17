class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
def insertAtFront(head, val): # Time, Space Complexities: O(1), O(1)
    new_node = Node(val)

    #1. Link new node to current head
    new_node.next = head

    #2. Update current head's prev pointer if list is not empty
    if head is not None:
        head.prev = new_node

    return new_node 

def insertAtBack(head, tail, val): # Time, Space Complexities: O(1), O(1)
    new_node = Node(val)

    #1. Handle empty list
    if head is None:
        return new_node
    
    #2. Link tail and new node together
    tail.next = new_node
    new_node.prev = tail
    return head

def insertAfter(head, val, loc): # Time, Space Complexities: O(1), O(1)
    if loc is None:
        return head
    new_node = Node(val)

    #1. Set new node pointers to bridge the gap
    new_node.next = loc.next
    new_node.prev = loc

    #2. Update following node's prev pointer if it exists
    if loc.next is not None:
        loc.next.prev = new_node

    #3. Update loc's next pointer
    loc.next = new_node

    return head

def insertBefore(head, val, loc): # Time, Space Complexities: O(1), O(1)
    if head is None or loc is None:
        return head
    
    #1. Handle inserting before the head
    if head == loc:
        return insertAtFront(head, val)
    new_node = Node(val)

    #2. Re-link pointers to insert new node between loc.prev and loc
    new_node.next = loc
    new_node.prev = loc.prev
    loc.prev.next = new_node
    loc.prev = new_node

    return head

def deleteFront(head): # Time, Space Complexities: O(1), O(1)
    if head is None:
        return head
    new_head = head.next

    #1. Clear the prev pointer of the new head
    if new_head is not None:
        new_head.prev = None

    return new_head

def deleteBack(head, tail): # Time, Space Complexities: O(1), O(1)
    if head is None or tail is None:
        return None
    
    #1. Handle single node list
    if head == tail:
        return None
    
    #2. Move tail back and sever the link
    new_tail = tail.prev
    new_tail.next = None

    return head

def deleteNode(head, loc): # Time, Space Complexities: O(1), O(1)
    if head is None or loc is None:
        return head
    
    #1. Handle deleting the head
    if head == loc:
        return deleteFront(head)
    
    #2. Link loc's neighbors to each other
    loc.prev.next = loc.next
    if loc.next is not None:
        loc.next.prev = loc.prev
    
    return head

def length(head): # Time, Space Complexities: O(n), O(1)
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    
    return count

def reverseIterative(head): # Time, Space Complexities: O(n), O(1)
    curr = head
    new_head = head

    #1. Swap next and prev pointers for every node
    while curr is not None:
        new_head = curr
        curr.next, curr.prev = curr.prev, curr.next
        curr = curr.prev # Moving forward in original list is now .prev
    
    return new_head

def reverseRecursive(head): # Time, Space Complexities: O(n), O(n)
    
    #1. Helper to swap pointers through recursion
    def _reverse(curr):
        if curr is None:
            return None
        
        #2. Swap current node pointers
        curr.next, curr.prev = curr.prev, curr.next
        
        #3. Return curr if it was the last node (now the new head)
        if curr.prev is None:
            return curr
        return _reverse(curr.prev)
    
    return _reverse(head)
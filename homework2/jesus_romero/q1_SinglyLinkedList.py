class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def insertAtFront(head, val): # Time, Space Complexities: O(1), O(1).
    new_node = Node(val)
    new_node.next = head
    return new_node 


def insertAtBack(head, val): # Time, Space Complexities: O(n), O(1).
    new_node = Node(val)
    
    #1. Edge Case, if the list is empty, the new node becomes the head
    if head is None:
        return new_node
    
    #2. Traverse to the end of the list
    current = head
    while current.next is not None:
        current = current.next
    
    #3. Link the last node to the new node
    current.next = new_node
    
    #4. Return the original head (as the start of the list hasn't changed)
    return head

def insertBefore(head, val, loc): # Time, Space Complexities: O(n), O(1).
    #1. EC Handle empty list or invalid loc
    if head is None or loc is None:
        return head

    #2. Handle the edge case: loc is the first node
    if head == loc:
        new_node = Node(val)
        new_node.next = head
        return new_node

    #3. Traverse to find the node BEFORE loc
    current = head
    while current is not None and current.next != loc:
        current = current.next

    #4. If current is None, loc wasn't found in the list
    if current is None:
        return head

    #5. Insert the new node
    new_node = Node(val)
    new_node.next = loc
    current.next = new_node

    return head

def deleteFront(head): # Time, Space Complexities: O(1), O(1).
    #1. EC Handle empty list or invalid loc
    if head is None:
        return head

    #2. Normal case
    return head.next

def deleteBack(head): # Time, Space Complexities: O(n), O(1).
    #1. Empty list
    if head is None:
        return None
    
    #2. Only one node in the list
    if head.next is None:
        return None
    
    #3. Multiple nodes
    current = head
    # Traverse until current is the second to last node
    while current.next.next is not None:
        current = current.next

    current.next = None
    return head

def deleteNode(head, loc): # Time, Space Complexities: O(n), O(1).
    #1. Empty list or invalid target
    if head is None or loc is None:
        return head
    
    #2. Target is the head node
    if head == loc:
        return head.next
    
    #3. Traverse to find the node BEFORE loc
    current = head
    while current.next is not None and current.next != loc:
        current = current.next
    
    #4. Loc not found in the list
    if current.next is None:
        return head
    
    #5. Bridge the gap (Skip over loc)
    current.next = loc.next
    
    return head

def reverseIterative(head): # Time, Space Complexities: O(n), O(1).
    #1. Initialize prev to None and curr to head
    prev = None
    curr = head
    
    #2. Loop until curr becomes None
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        
    #3. Return prev as it is the new head of the reversed list
    return prev

def reverseRecursive(head): # Time, Space Complexities: O(n), O(n).
    #1. Define a helper to pass the 'prev' state through the stack
    def _reverse(curr, prev):
        #2. Base case: if curr is None, we have reached the new head
        if not curr:
            return prev
        
        #3. Save the next node and flip the current pointer
        nxt = curr.next
        curr.next = prev
        
        #4. Recurse forward with the updated pointers
        return _reverse(nxt, curr)

    #5. Start recursion with the initial head and None as the previous node
    return _reverse(head, None)

def length(head): # Time, Space Complexities: O(n), O(1).
    #1. Initialize counter and current pointer
    count = 0
    current = head
    
    #2. Traverse entire list
    while current is not None:
        count += 1
        current = current.next
        
    #3. Return the final count
    return count
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Creates a new node with data 'val' at front; Returns the head. O(1) time.
def insertAtFront(head, val):

    newHead = Node(val)

    newHead.next = head # Works even if head is None/Null

    return newHead


# Creates a new node with data 'val' at end; Returns head. O(n) time.
def insertAtBack(head, val):

    newNode = Node(val)

    if head == None:
        return newNode
    else:
        walker = head

        while walker.next:
            walker = walker.next

        # Now walker is on last node

        walker.next = newNode

        return head



# Creates new node with data 'val' after node loc; Returns head. O(1) time.
def insertAfter(head, val, loc):

    if loc == None:
        return head

    if head == None:
        # There is nothing to insert after
        return head
    
    # Now we know loc and head are defined Nodes
    newNode = Node(val)

    newNode.next = loc.next

    loc.next = newNode

    return head
    

# Creates new node with data 'val' before node loc; Returns head. O(n) time.
def insertBefore(head, val, loc):

    if loc == None:
        return head
    
    if head == None:
        return head
    
    newNode = Node(val)
    
    if loc == head:
        newNode.next = head
        return newNode
    
    
    walker = head
    # Walk until we find loc or until we go to the end of the list. Maybe loc is not in the list
    while walker.next != loc and walker.next != None:
        walker = walker.next

    if walker.next == None:
        # loc was not in the list, so do not attach the node anywhere
        return head

    # Now walker.next points to loc
    newNode.next = loc

    walker.next = newNode

    return head


# Removes first node; Returns head. O(1) time.
def deleteFront(head):

    if head == None or head.next == None:
        return None
    
    newHead = head.next

    return newHead


# Removes last node; Returns head. O(n) time.
def deleteBack(head):

    if head == None or head.next == None:
        return None
    
    if head.next.next == None:
        head.next = None
        return head
    
    # We want the walker to stop at the node right before the last node
    walker = head

    while walker.next.next:
        walker = walker.next

    walker.next = None

    return head



# Deletes node loc; Returns head. O(n) time
def deleteNode(head, loc):

    if head == None or loc == None:
        return head
    
    if loc == head:
        newHead = head.next
        loc.next = None
        return newHead


    # Now we know loc and head is defined, AND loc is not the same node as head

    walker = head
    # Walk until we find loc or until we reach the end of the list
    while walker.next != loc and walker.next != None:
        walker = walker.next

    if walker.next == None:
        # loc is not in the linked list, don't delete anything
        return head
    
    # Now walker.next points to loc... make walker.next point to the node after loc to remove loc from the linked list
    walker.next = walker.next.next

    return head



# Returns length of list. O(n) time
def length(head):
    count = 0
    walker = head

    while walker:
        count += 1
        walker = walker.next

    return count


# Reverses the linked list iteratively. O(n) time.
def reverseIterative(head):

    if head == None or head.next == None:
        return head

    prev = None
    curr = head

    while curr:
        # Next node
        forward = curr.next

        # Reverse
        curr.next = prev

        # The new 'previous' node is now the current node (To set up next iteration correctly)
        prev = curr

        # Move curr forward
        curr = forward

    return prev


# Reverses the linked list recursively. O(n) time.
def reverseRecursive(head):
    
    if head == None or head.next == None:
        return head
    
    def reverse(curr, prev):

        if curr == None:
            # Nothing more to reverse, return the node that prev is at
            return prev

        # next Node
        forward = curr.next

        # Reverse
        curr.next = prev

        # Recurse of the rest of the list
        return reverse(forward, curr)
    
    return reverse(head, None)


    
    
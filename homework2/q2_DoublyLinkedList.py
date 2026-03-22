class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Creates a new node with data 'val' at front; Returns the head. O(1) time.
def insertAtFront(head, val):

    newHead = Node(val)

    newHead.next = head
    # newHead prev will continue to point at None/Null since we are making a new head node

    if head:
        head.prev = newHead

    return newHead


# Creates a new node with data 'val' at end; Returns head. O(1) time.
def insertAtBack(head, tail, val):

    newTail = Node(val)

    if not head and not tail: # empty list
        return newTail
    
    # There is no specification on how to handle cases when either head OR tail is Null while the the other is defined...
    # If that happens then the user is not maintaining the list correctly

    newTail.prev = tail
    # newTail next will continue to point at None/Null

    tail.next = newTail

    tail = newTail

    return head


# Creates new node with data 'val' after node loc; Returns head. O(1) time.
def insertAfter(head, val, loc):

    if head == None or loc == None:
        return head
    
    newNode = Node(val)

    newNode.next = loc.next
    newNode.prev = loc

    if loc.next:
        loc.next.prev = newNode

    loc.next = newNode

    return head
    

# Creates new node with data 'val' before node loc; Returns head. O(1) time.
def insertBefore(head, val, loc):

    if head == None or loc == None:
        return head
    
    newNode = Node(val)

    newNode.next = loc
    newNode.prev = loc.prev

    if loc.prev:
        loc.prev.next = newNode
    else:
        # loc == head
        head = newNode

    loc.prev = newNode

    return head



# Removes first node; Returns head. O(1) time.
def deleteFront(head):

    if head == None:
        return head
    
    # head is the only node
    if not head.next:
        return None
    else:
        # there is at least one other node other than head
        newHead = head.next

        head.next = None
        newHead.prev = None

        return newHead




# Removes last node; Returns head. O(1) time.
def deleteBack(head, tail):

    if head == None and tail == None: # empty list
        return head
    

    if tail == head:
        return None
    
    newTail = tail.prev
    tail.prev = None
    newTail.next = None

    tail = newTail

    return head






# Deletes node loc; Returns head. O(1) time
def deleteNode(head, loc):

    if head == None or loc == None:
        return head
    
    # Case where loc is first node
    if loc == head:

        if head.next:
            newHead = head.next
            newHead.prev = None
            head.next = None

            return newHead
        else:
            # loc is the only node in linked list
            return None

    # Regular Case
    loc.prev.next = loc.next
    
    if loc.next:
        loc.next.prev = loc.prev

    loc.next = None
    loc.prev = None

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
    
    temp = None

    curr = head

    while curr:
        # Swap references of next and prev
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp

        # Keep iterating
        curr = curr.prev

    if temp:
        # In regular cases, temp stops at the original 2nd to last node... because we swapped references, the original last node is on temp.prev
        head = temp.prev

    return head


# Reverses the linked list recursively. O(n) time.
def reverseRecursive(head):
    
    if head == None or head.next == None:
        return head
    
    def reverse(node):

        if node == None:
            return None
        
        # Swap next and prev reference
        temp = node.prev
        node.prev = node.next
        node.next = temp

        # If prev is now None, then we have reached the end of the original list and found the new head
        if node.prev == None:
            return node
        else:
            # Keep recursing
            return reverse(node.prev)
        
    
    return reverse(head)
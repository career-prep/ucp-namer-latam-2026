class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Time complexity: O(1)
def insertAtFront(head, val):
    newNode = Node(val)

    if head:
        newNode.next = head
        head.prev = newNode

    return newNode

# Time complexity: O(1)
def insertAtBack(head, tail, val):
    newNode = Node(val)

    if head is None:
        return newNode
    
    tail.next = newNode
    newNode.prev = tail

    return head

# Time complexity: O(1)
def insertAfter(head, val, loc):
    if not loc:
        return head
    
    newNode = Node(val)
    newNode.next = loc.next
    newNode.prev = loc

    if loc.next:
        loc.next.prev = newNode

    loc.next = newNode

    return head

# Time complexity: O(1)
def insertBefore(head, val, loc):
    if not loc:
        return head
    
    newNode = Node(val)
    newNode.next = loc
    newNode.prev = loc.prev

    if loc.prev:
        loc.prev.next = newNode
    loc.prev = newNode
    
    return newNode if head == loc else head

# Time complexity: O(1)
def deleteFront(head):
    if not head or not head.next:
        return None
    
    newHead = head.next
    newHead.prev = None

    return newHead

# Time complexity: O(1)
def deleteBack(head, tail):
    if not head:
        return None
    
    if head == tail:
        return None

    tail.prev.next = None
    return head

# Time complexity: O(1)
def deleteNode(head, loc):
    if not loc:
        return head
    
    if not loc.prev:
        return deleteFront(head)
    
    if loc.next:
        loc.next.prev = loc.prev

    loc.prev.next = loc.next

    return head

# Time complexity: O(n)
def length(head):
    count = 0

    curr = head
    while curr:
        count += 1
        curr = curr.next

    return count

# Time complexity: O(n)
def reverseIterative(head):
    curr = head
    newHead = None

    while curr:
        curr.prev, curr.next = curr.next, curr.prev
        newHead = curr
        curr = curr.prev

    return newHead

# Time complexity: O(n)
def reverseRecursive(head):
    def helper(curr):
        if not curr:
            return None
        
        curr.prev, curr.next = curr.next, curr.prev

        if not curr.prev:
            return curr
        
        return helper(curr.prev)
    
    return helper(head)


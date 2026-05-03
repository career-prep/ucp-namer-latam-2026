class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Time complexity: O(1)
def insertAtFront(head, val):
    newNode = Node(val)
    newNode.next = head
    return newNode

# Time complexity: O(n)
def insertAtBack(head, val):
    newNode = Node(val)
    if not head:
        return newNode
    
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = newNode
    return head

# Time complexity: O(1)
def insertAfter(head, val, loc):
    if not loc:
        return head
    
    newNode = Node(val)
    newNode.next = loc.next
    loc.next = newNode
    return head

# Time complexity: O(n)
def insertBefore(head, val, loc):
    if not head:
        return None
    
    if head == loc:
        return insertAtFront(head, val)
    
    curr = head
    while curr.next and curr.next != loc:
        curr = curr.next

    if curr.next is None:
        return head

    newNode = Node(val)
    curr.next = newNode
    newNode.next = loc
    return head

# Time complexity: O(1)
def deleteFront(head):
    if not head:
        return None
    return head.next

# Time complexity: O(n)
def deleteBack(head):
    if not head or not head.next:
        return None
    
    curr = head
    while curr.next.next:
        curr = curr.next

    curr.next = None
    return head

# Time complexity: O(n)
def deleteNode(head, loc):
    if not head:
        return None
    
    if head == loc:
        return deleteFront(head)
    
    curr = head
    while curr.next and curr.next != loc:
        curr = curr.next

    if curr.next is None:
        return head
    
    curr.next = loc.next
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
    prev = None
    curr = head

    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode

    return prev

# Time complexity: O(n)
def reverseRecursive(head):
    def helper(curr, prev):
        if not curr:
            return prev
        
        nextNode = curr.next
        curr.next = prev
        
        return helper(nextNode, curr)
    
    return helper(head, None)


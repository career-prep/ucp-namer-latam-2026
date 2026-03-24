class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Time Complexity: O(1)
def insertAtFront(head, val):
    return Node(val, head)

# Time Complexity: O(n)
def insertAtBack(head, val):
    temp = Node(val)
    if head is None:
        return temp
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = temp
    return head

# Time Complexity: O(1)
def insertAfter(head, val, loc):
    temp = Node(val, loc.next)
    loc.next = temp
    return head

# Time Complexity: O(n)
def insertBefore(head, val, loc):
    temp = Node(val)

    if loc == head:
        temp.next = head
        head = temp
        return head

    curr = head
    while curr.next != loc:
        curr = curr.next
    curr.next = temp
    temp.next = loc
    return head

# Time Complexity: O(1)
def deleteFront(head):
    if head is None:
        return None
    head = head.next
    return head

# Time Complexity: O(n)
def deleteBack(head):
    if head is None or head.next is None:
        return None

    curr = head
    while curr.next.next is not None:
        curr = curr.next
    curr.next = None
    return head

# Time Complexity: O(n)
def deleteNode(head, loc):
    if head is None:
        return None
    if loc == head:
        head = head.next
        return head
    curr = head
    while curr.next != loc:
        curr = curr.next
    curr.next = loc.next
    return head

# Time Complexity: O(n)
def length(head):
    curr = head
    count = 0
    while curr != None:
        curr = curr.next
        count += 1
    return count

# Time Complexity: O(n)
def reverseIterative(head):
    prev = None
    curr = head
    while curr is not None:
        curr_next = curr.next
        curr.next = prev
        prev = curr
        curr = curr_next
    return prev

# Time Complexity: O(n)
def reverseHelper(curr):
    if curr.next is None:
        return curr

    tail = reverseHelper(curr.next)
    curr.next.next = curr
    curr.next = None
    return tail

# Time Complexity: O(n)
def reverseRecursive(head):
    if head is None:
        return None
    return reverseHelper(head)
class Node:
  def __init__(self, data, next=None, prev=None):
    self.data = data
    self.next = next
    self.prev = prev

# Time Complexity: O(1)
def insertAtFront(head, val):
    temp = Node(val, head)
    if head is not None:
        head.prev = temp
    head = temp
    return head

# Time Complexity: O(1)
def insertAtBack(head, tail, val):
    temp = Node(val)
    if head is None:
        return temp, temp
    tail.next = temp
    temp.prev = tail
    tail = temp
    return head, tail

# Time Complexity: O(1)
def insertAfter(head, val, loc):
    temp = Node(val, loc.next, loc)
    if loc.next is not None:
        loc.next.prev = temp
    loc.next = temp
    return head

# Time Complexity: O(1)
def insertBefore(head, val, loc):
    temp = Node(val, loc, loc.prev)
    if loc.prev is not None:
        loc.prev.next = temp
    else:
        head = temp
    loc.prev = temp
    return head

# Time Complexity: O(1)
def deleteFront(head):
    if head is None:
        return None
    if head.next is None:
        return None
    head = head.next
    head.prev = None
    return head

# Time Complexity: O(1)
def deleteBack(head, tail):
    if head is None:
        return None, None
    if head.next is None:
        return None, None
    tail = tail.prev
    tail.next = None
    return head, tail

# Time Complexity: O(1)
def deleteNode(head, loc):
    if head is None:
        return None
    if loc == head:
        head = head.next
        if head is not None:
            head.prev = None
        return head
    if loc.next is not None:
        loc.next.prev = loc.prev
    if loc.prev is not None:
        loc.prev.next = loc.next
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
    curr = head
    new_head = None
    while curr is not None:
        curr.next, curr.prev = curr.prev, curr.next
        new_head = curr
        curr = curr.prev
    head = new_head
    return head

# Time Complexity: O(n)
def reverseHelper(curr):
    if curr is None:
        return None
    curr.next, curr.prev = curr.prev, curr.next
    if curr.prev is None:
        return curr
    return reverseHelper(curr.prev)

# Time Complexity: O(n)
def reverseRecursive(head):
    return reverseHelper(head)
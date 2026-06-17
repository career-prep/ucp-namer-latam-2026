'''
Time: 40 min
'''

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def insertAtFront(head, val):
    newhead = Node(val)
    newhead.next = head
    return newhead

def insertAtBack(head, val):
    if head == None:
        return Node(val)
    
    cur = head
    while cur.next:
        cur = cur.next

    cur.next = Node(val)
    return head

def insertAfter(head, val, loc):
    newNode = Node(val)
    temp = loc.next
    loc.next = newNode
    newNode.next = temp
    
    return head

def insertBefore(head, val, loc):
    if head == None:
        return None
    
    cur = head
    prev = None
    while cur and cur is not loc:
        prev = cur
        cur = cur.next
    if cur is None:
        return head
    newNode = Node(val)
    prev.next = newNode
    newNode.next = cur
    return head

def deleteFront(head):
    if head == None:
        return None
    return head.next

def deleteBack(head):
    if head == None or head.next == None:
        return None
    cur = head
    while cur.next.next:
        cur = cur.next
    cur.next = None
    return head

def deleteNode(head, loc):
    if head == None:
        return None
    if head is loc:
        return head.next
    cur = head
    prev = None
    while cur and cur is not loc:
        prev = cur
        cur = cur.next
    if cur is None:
        return head
    prev.next = cur.next
    return head

def length(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count

def reverseIterative(head):
    if head == None:
        return None
    cur = head
    prev = None
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev

def reverseRecursive(head):
    if head == None:
        return None
    return recursiveSwap(head, None)

def recursiveSwap(cur, prev):
    if cur == None:
        return prev
    newNode = cur.next
    cur.next = prev

    return recursiveSwap(newNode, cur)

def print_list(head):
    linked_list = []
    while head:
        linked_list.append(head.data)
        head = head.next
    print(linked_list)

head = Node(1)
node2 = Node(2)
head.next = node2
print_list(head)
head = insertAtFront(head, 0)
insertAtBack(head, 4)
insertAfter(head, 3, node2)
insertAfter(head, 5, Node(5)) # Check if inserting after nonexisting node works
print_list(head)

insertBefore(head, 1, node2)
head = deleteFront(head)
deleteBack(head)
deleteNode(head, node2)
print_list(head)
print(length(head))
head = reverseIterative(head)
print_list(head)
print_list(reverseRecursive(head))

head1 = None
head1 = deleteFront(head1)
print_list(head1)
deleteBack(head1)
print_list(head1)

head1 = Node(2)
head1 = deleteFront(head1)
print_list(head1)

# ------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.head = None
    
    def insertAtFront(head, val):
        newHead = Node(val)
        newHead.next = head
        return newHead
    
    def insertAtBack(head, val):
        newNode = Node(val)
        # Case 1: No Head
        if head is None:
            head = newNode
        # Case 2: head exist
        cur = head
        while cur.next:
            cur = cur.next
        cur.next = newNode
        return head
    
    def insertAfter(head, val, loc):
        # Case 1: loc is none
        if loc is None:
            return head
        # Case 2: loc exists
        newNode = Node(val)
        temp = loc.next
        loc.next = newNode
        newNode.next = temp
        return head
    
    def insertBefore(head, val, loc):
        # Case 1: head is none
        if head is None:
            return None
        # Case 2: loc is none
        if loc is None:
            return None
        # Case 3: loc exists
        
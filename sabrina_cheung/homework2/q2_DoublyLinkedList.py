'''
Time: 30 mins
'''

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

def insertAtFront(head, val):
    newhead = Node(val)
    newhead.next = head
    if head:
        head.prev = newhead
    return newhead

def insertAtBack(head, val):
    if head == None:
        return Node(val)
    
    cur = head
    while cur.next:
        cur = cur.next

    cur.next = Node(val)
    cur.next.prev = cur
    return head

def insertAfter(head, val, loc):
    newNode = Node(val)
    temp = loc.next
    loc.next = newNode
    newNode.next = temp
    newNode.prev = loc

    if temp:
        temp.prev = newNode

    return head

def insertBefore(head, val, loc):
    new = Node(val)
    
    new.prev = loc.prev
    new.next = loc
    
    if loc.prev:
        loc.prev.next = new
    else:
        head = new
    
    loc.prev = new
    
    return head

def deleteFront(head):
    if head == None or head.next == None:
        return None

    head.next.prev = None
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
        if head.next:
            head.prev = None
        return head.next
    
    if loc.next:
        loc.next.prev = loc.prev
    if loc.prev:
        loc.prev.next = loc.next
    return head

def length(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count

def reverseIterative(head):
    if head == None or head.next == None:
        return head
    cur = head
    prev = None
    while cur:
        temp = cur.next
        cur.next = prev
        cur.prev = temp
        
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
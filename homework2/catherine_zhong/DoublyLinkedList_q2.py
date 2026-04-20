class Node:
    def __init__ (self, data):
        self.val = data
        self.next = None
        self.prev = None

#creates new Node with data val at front; returns head. O(1) time.
def insertAtFront(head, val):
    newhead = Node(val)
    newhead.next = head

    if head:
        head.prev = newhead

    return newhead

#creates new Node with data val at end; returns head. O(n) time.
def insertAtBack(head, val):
    if head == None:
        head = Node(val)
        return head

    current = head
    while current.next != None:
        current = current.next

    current.next = Node(val)
    current.next.prev = current
    return head

#creates new Node with data val after Node loc; returns head. O(1) time.
def insertAfter(head, val, loc):
    newNode = Node(val)

    newNode.next = loc.next
    newNode.prev = loc

    if loc.next:
        loc.next.prev = newNode

    loc.next = newNode
    return head

#creates new Node with data val before Node loc; returns head. O(n) time.
def insertBefore(head, val, loc):
    if not loc:
        return head

    newNode = Node(val)

    if loc == head:
        newNode.next = head
        head.prev = newNode
        return newNode

    prevNode = loc.prev
    prevNode.next = newNode
    newNode.prec = prevNode

    newNode.next = loc
    loc.prev = newNode

    return head

#removes first Node; returns head. O(1) time.
def deleteFront(head):
    if head is None:
        return None

    if head.next is None:
        return None

    head = head.next
    head.prev = None
    return head


#removes last Node; returns head. O(n) time.
def deleteBack(head):
    if head == None:
        return None

    if head.next == None:
        return None

    current = head
    while current.next.next != None:
        current = current.next
    current.next.prev = None
    current.next = None

    return head

#deletes Node loc; returns head. O(n) time.
def deleteNode(head, loc):
    if head == loc:
        head = head.next
        if head:
            head.prev = None
        return head

    if loc.next:
        loc.next.prev = loc.prev

    if loc.prev:
        loc.prev.next = loc.next

    return head

#returns length of the list. O(n) time.
def length(head):
    lengthList = 0

    while head != None:
        lengthList += 1
        head = head.next
    return lengthList

#reverses the linked list iteratively. O(n) time.
def reverseIterative(head):
    current = head 
    temp = None 

    while current:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev

    if temp:
        head = temp.prev

    return head

#reverses the linked list recursively (Hint: you will need a helper function.) O(n) time.
def reverseRecursive(head):
    if head is None:
        return None

    temp = head.prev
    head.prev = head.next
    head.next = temp 
    if head.prev is None:
        return head

    
    return reverseRecursive(head.prev)


def printList(head):
    data = []
    current = head
    while current != None:
        data.append(current.val)
        current = current.next

    print(", ".join(str(item) for item in data))

head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

head.next = node2
node2.prev = head
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
node4.next = node5
node5.prev= node4

print('original list: ')
printList(head)

head = insertAtFront(head, 0)
print('insert 0 at front of list: ')
printList(head)

head = insertAtBack(head, 6)
print('insert 6 at back of list: ')
printList(head)

head = insertAfter(head, 0, node2)
print('insert 0 after node 2: ')
printList(head)

head = insertBefore(head, 0, node4)
print('insert 0 before node 4: ')
printList(head)

head = deleteFront(head)
print('delete front node: ')
printList(head)

head = deleteBack(head)
print('delete last node: ')
printList(head)

head = deleteNode(head, node2.next)
print('delete 3rd node: ')
printList(head)

print('length of list: ')
print(length(head))

head = reverseIterative(head)
print('reverse list interatively: ')
printList(head)

head = reverseRecursive(head)
print('reverse list recursively: ')
printList(head)
#time spent: 40 mins
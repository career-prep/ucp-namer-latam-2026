class Node:
    def __init__ (self, data):
        self.val = data
        self.next = None

#creates new Node with data val at front; returns head. O(1) time.
def insertAtFront(head, val):
    newhead = Node(val)
    newhead.next = head
    head = newhead
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
    return head

#creates new Node with data val after Node loc; returns head. O(1) time.
def insertAfter(head, val, loc):
    if head == None:
        return Node(val)

    current = head
    while current != loc:
        current = current.next

    temp = current.next
    newNode = Node(val)
    current.next = newNode
    newNode.next = temp
    return head

#creates new Node with data val before Node loc; returns head. O(n) time.
def insertBefore(head, val, loc):
    if head == None:
        return Node(val)

    current = head
    while current.next != loc:
        current = current.next

    temp = current.next
    newNode = Node(val)
    current.next = newNode
    newNode.next = temp

    return head

#removes first Node; returns head. O(1) time.
def deleteFront(head):
    return head.next


#removes last Node; returns head. O(n) time.
def deleteBack(head):
    if head == None:
        return None

    if head.next == None:
        return None

    current = head
    while current.next.next != None:
        current = current.next
    current.next = None

    return head

#deletes Node loc; returns head. O(n) time.
def deleteNode(head, loc):
    if head == loc:
        return head.next

    current = head
    while current.next != loc:
        current = current.next
    current.next = current.next.next
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
    if head == None:
        return None 

    prev = None
    while head:
        temp = head
        head = temp.next
        temp.next = prev
        prev = temp
    return prev

#reverses the linked list recursively (Hint: you will need a helper function.) O(n) time.
def reverseRecursive(head):
    return swapNodes(head)

def swapNodes(head):
    if head == None or head.next == None:
        return head
    else:
        reverse = swapNodes(head.next)
        head.next.next = head
        head.next = None
        return reverse

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
node2.next = node3
node3.next = node4
node4.next = node5

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
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


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def front(self):
        if self.head:
            return self.head.val

        return

    def back(self):
        if self.tail:
            return self.tail.val

        return

    def pushBack(self, x):
        temp = Node(x)

        if not self.head:
            self.head = self.tail = temp
            return

        self.tail.next = temp
        self.tail = temp

    def pushFront(self, x):
        self.head = insertAtFront(self.head, x)

        if self.tail is None:
            self.tail = self.head

    def popFront(self):
        if self.head is None:
            return 
        result = self.head.val
        self.head = deleteFront(self.head)
        if self.head is None:
            self.tail = None

        return result


    def popBack(self):
        if not self.tail:
            return

        result = self.tail.val
        
        if self.head == self.tail:
            self.head = self.tail = None
            return result

        self.tail = self.tail.prev
        self.tail.next = None

        return result

    def isEmpty(self):
        return self.head == None

    def printDeque(self):
        result = []

        current = self.head
        while current:
            result.append(current.val)
            current = current.next

        print(', '.join(str(i) for i in result))

deque = Deque()

deque.pushBack(1)
deque.pushBack(2)
deque.pushBack(3)
deque.pushBack(4)
deque.pushBack(5)

print('initial deque: ')
deque.printDeque()

print('get front item in deque: ')
print(deque.front())

print('get back item in deque: ')
print(deque.back())

print('pop front item in deque: ')
print('popped item: ', deque.popFront())
print('current deque: ')
deque.printDeque()

print('pop back item in deque: ')
print('popped item: ', deque.popBack())
print('current deque: ')
deque.printDeque()

print('check if deque is empty: ')
print(deque.isEmpty())

#time spent: 30min
class Node:
    def __init__ (self, data):
        self.val = data
        self.next = None

#creates new Node with data val at front; returns head. O(1) time.
def insertAtFront(head, val):
    newhead = Node(val)
    newhead.next = head

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



class Queue:
    def __init__ (self):
        self.head = None
        self.tail = None

    def peek(self):
        return self.head

    def enqueue(self, x):
        if self.head == None:
            self.head = Node(x)
            self.tail = self.head
            return

        self.tail.next = Node(x)
        self.tail = self.tail.next

    def dequeue(self):
        val = self.head.val
        self.head = self.head.next
        return val

    def isEmpty(self):
        return self.head == None

    def printQueue(self):
        elements = []

        current = self.head
        while current != None:
            elements.append(current.val)
            current = current.next

        print(', '.join(str(i) for i in elements))

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

print('initial queue: ')
queue.printQueue()

print('peek at first element: ')
print(queue.peek().val)

print('dequeue element: ')
print(queue.dequeue())

print('check if queue is empty: ')
print(queue.isEmpty())

#time spent: 15min
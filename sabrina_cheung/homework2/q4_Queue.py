'''
Time: 15 min
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

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def peek(self):
        return self.head.data
    
    def enqueue(self, x):
        if self.head == None:
            self.head = Node(x)
            self.tail = self.head
            return
        
        self.tail.next = Node(x)
        self.tail = self.tail.next

    def dequeue(self):
        if self.head == None:
            return None
        val = self.head.data
        self.head = self.head.next
        return val
    
    def isEmpty(self):
        return self.head == None
    
    def printQueue(self):
        queue_list = []
        cur = self.head
        while cur:
            queue_list.append(cur.data)
            cur = cur.next
        print(queue_list) 
    
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.printQueue()

print(queue.peek())
print(queue.dequeue())
print(queue.isEmpty())
print(queue.dequeue())
queue.printQueue()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# insert at front
def insertatfront(head, val):
    new_node = Node(val)
    if head != None:
        head.prev = new_node  
        new_node.next = head 
    head = new_node
    return head


# insert at the end
def insertatback(head, val):
    curr = head
    newNode = Node(val)

    if head == None:
        return newNode

    while curr.next:
        curr = curr.next
    curr.next = newNode
    newNode.prev = curr        

    return head


# insert after Node loc
def insertAfter(head, val, loc):
    newNode = Node(val)
    newNode.next = loc.next
    newNode.prev = loc         
    if loc.next != None:
        loc.next.prev = newNode  
    loc.next = newNode
    return head


# insert before Node loc
def insertBefore(head, val, loc):
    newNode = Node(val)

    if head == loc:
        newNode.next = head
        head.prev = newNode    
        return newNode

    curr = head
    while curr.next != loc:
        curr = curr.next
    newNode.next = loc
    newNode.prev = curr        
    curr.next = newNode
    loc.prev = newNode         
    return head


# remove first node
def deleteFront(head):
    head = head.next
    if head != None:
        head.prev = None       
    return head


# remove last node
def deleteBack(head):

    if head.next == None:
        return None

    curr = head
    while curr.next.next != None:
        curr = curr.next
    curr.next = None
    return head


# delete node loc
def deleteNOde(head, loc):
    if head == loc:
        return head.next

    curr = head
    while curr.next != loc:
        curr = curr.next
    curr.next = curr.next.next
    if curr.next != None:
        curr.next.prev = curr  
    return head


# return length of the list  
def length(head):
    l = 0
    curr = head
    while curr != None:
        curr = curr.next
        l += 1
    return l


# reverse the linkedlist iteratively
def reverseIterative(head):
    prev = None
    nxt = None
    curr = head

    while curr != None:
        nxt = curr.next
        curr.next = prev
        curr.prev = nxt        
        prev = curr
        curr = nxt
    return prev


# reverse the linkedlist recursively
def reverseRecursive(head):
    def helper(curr, prev):
        if curr == None:
            return prev
        nxt = curr.next
        curr.next = prev
        curr.prev = nxt        
        return helper(nxt, curr)

    return helper(head, None)

# time taken- around 20 mins
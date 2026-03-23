class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# insert at front
def insertatfront(head, val):
    new_node = Node(val)
    new_node.next= head 
    head = new_node
    return head 

# insert at the end
def insertatback(head, val):
    curr= head 
    newNode= Node(val)

    if head is None:
        return newNode

    while curr.next:
        curr= curr.next
    curr.next= newNode

    return head 

# insert after Node loc
def insertAfter(head, val, loc):
    newNode  = Node(val)
    newNode.next= loc.next
    loc.next= newNode
    return head 

# TEST CASE
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

head = node1

# insert 10 after node2
head = insertAfter(head, 10, node2)

# print result
curr = head
while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
print("None")


# insert before Node loc
def insertBefore(head, val, loc):
    newNode= Node(val)

    # if inserting before the head
    if head == loc:
        newNode.next= head 
        return newNode

    curr= head 
    while curr.next != loc:
        curr= curr.next 
    newNode.next= loc 
    curr.next= newNode 
    return head 

# remove first node
def deleteFront(head):
    head= head.next
    return head 

# remove last node
def deleteBack(head):

    if head.next is None:
        return None

    curr= head 
    while curr.next.next != None:
        curr= curr.next
    curr.next= None
    return head

# delete node noc
def deleteNOde(head, loc):
    if head == loc:
        return head.next

    curr= head 
    while curr.next != loc:
        curr= curr.next 
    curr.next= curr.next.next 
    return head 

# return length of the list
def deleteNode(head):
    l =0 
    curr= head
    while curr != None:
        curr = curr.next
        l += 1 
    return l 

# reverse the linkedlist iteratively
def reverseIterative(head):
    prev= None
    nxt= None 
    curr = head 

    while curr != None:
        nxt = curr.next 
        curr.next = prev
        prev= curr 
        curr = nxt 
    return prev 

# reverse the linkedlist recursively
def reverseRecursive(head):
    def helper(curr, prev):
        if curr is None:
            return prev 
        nxt = curr.next 
        curr.next= prev 
        return helper(nxt, curr)
    
    return helper(head, None)


# time taken- around 40 mins
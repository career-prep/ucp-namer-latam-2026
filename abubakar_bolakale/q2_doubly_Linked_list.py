class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
def insert_at_front(head, val):
    new_node = Node(val) 
    if head is not None: 
        head.prev = new_node
        new_node.next = head 
    head = new_node 
    return new_node     
    #time complexity = 0(1)
    #space complexity = 0(n) 
    
def insert_at_back(head, val):
    new_node = Node(val)
    if head is None:
        return new_node
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = new_node
    new_node.prev = curr
    return head
    #time complexity = 0(n)
    #space complexity = 0(1)
def insert_after(head, val, location):
    curr = head
    while curr is not None:
        if curr.data == location:
            break
        curr = curr.next
    
    if curr is None:
        print("loction not found")
        return head
        
    new_node = Node(val)
    
    new_node.next = curr.next
    if curr.next is not None:
        curr.next.prev = new_node
    curr.next = new_node
    new_node.prev = curr
    
    return head

    #time complexity = 0(1)
    #space complexity = 0(1)

def insert_before(head, val, location):
    new_node = Node(val)
    if head is None:
        return None
    
    if head.data == location:
        new_node.next = head
        head.prev = new_node
        return new_node
    
    curr = head
    
    while curr is not None and curr.data != location:
        curr = curr.next
        
    if curr is None:
        print("Location not found")
        return head
    
    new_node.next = curr
    new_node.prev = curr.prev
    
    curr.prev.next = new_node
    curr.prev = new_node
 
    return head   
    #time complexity = 0(n)
    #space complexity = 0(1)
    
def delete_front(head):
    if head is None:
        return None
    new_head = head.next
    if head is not None:
        new_head.prev = None
    return new_head
#time complexity = 0(1)
#space complexity = 0(1)
 
def delete_back(head):
    if head is None:
        return None
    
    if head.next is None:
        return None
    
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.prev.next = None
    
    return head
#time complexity = 0(n)
#space complexity = 0(1)
 
def delete_at_node(head, pos):
    if head is None or pos <= 0:
        return head

    curr = head

    for _ in range(1, pos):
        if curr is None:
            return head 
        curr = curr.next

    if curr is None:
        return head

    if curr.prev is None:
        head = curr.next
        if head is not None:
            head.prev = None
        return head

    if curr.next is not None:
        curr.next.prev = curr.prev

    curr.prev.next = curr.next

    return head
    #time complexity = 0(n)
    #space complexity = 0(1)
    
def length(head):
    count = 0
    curr = head
    while curr is not None:
        count += 1
        curr = curr.next
    return count
    #time complexity = 0(n)
    #space complexity = 0(1)
    
def reverseIterative(head):
    # while head.next != None:
    #     head.prev, head.next, head = head.next, head.prev, head.next
        
    # head.next, head.prev = head.prev, None
    # return head
    
    p_curr = None
    curr = head
    
    while curr is not None:
        p_curr = curr.prev
        curr.prev = curr.next
        curr.next = p_curr        
                   
        curr = curr.prev
        
    if p_curr is not None:
        head = p_curr.prev      
    
    return head
    #time complexity = 0(n)
    #space complexity = 0(1)

def reverse_recursive(head):
    if head is None:
        return None

    temp = head.next
    head.next = head.prev
    head.prev = temp

    if head.prev is None:
        return head

    return reverse_recursive(head.prev)
    #time complexity = 0(n)
    #space complexity = 0(n)

def display(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" <-> ")
        curr = curr.next
    print("None")
    
head = None

head = insert_at_front(head, 10)
head = insert_at_front(head, 20)
head = insert_at_front(head, 30)
head = insert_at_front(head, 40)
head = insert_at_front(head, 50)

print("Doubly Linked List after front insertions:", end="")
display(head)

head = insert_at_back(head, 5)
head = insert_at_back(head, 3)
head = insert_at_back(head, 1)
print("Doubly Linked List after end insertions:" , end="")
display(head)

head = insert_after(head, 0, 10)
head = insert_after(head, 0, 1)
print("Doubly Linked List after insertions:" , end="")
display(head)

head = insert_before(head, 70, 50)
head = insert_before(head, 60, 50)
print("Doubly Linked List before insertions:" , end="")
display(head)

head = delete_front(head)
print("Doubly Linked List front deletion:" , end="")
display(head)

head = delete_back(head)
print("Doubly Linked List Back deletion:" , end="")
display(head)

head = delete_at_node(head, 2)
head = delete_at_node(head, 20)
print("Doubly Linked List Back deletion:" , end="")
display(head)

head = delete_at_node(head, 3)
print("Doubly Linked List Back deletion:" , end="")
display(head)

print("Linked List length: ", length(head))

head = reverseIterative(head)
print("Linked List reverse: ", end="")
display(head)

head = reverse_recursive(head)
print("Linked List reverse: ", end="")
display(head)
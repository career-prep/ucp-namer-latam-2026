class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def insert_at_front(head, val):
    new_node = Node(val)  
    new_node.next = head  
    return new_node     
    #time complexity = 0(1)
    #space complexity = 0(n)

def insert_at_end(head, val):
    new_node = Node(val)
    if head is None:
        return new_node
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = new_node
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
    curr.next = new_node
    return head
    #time complexity = 0(1)
    #space complexity = 0(1)

def insert_before(head, val, location):
    if head is None:
        return None
    
    if head.data == location:
        new_node = Node(val)
        new_node.next = head
        return new_node
    
    prev = None
    curr = head
    while curr is not None and curr.data != location:
        prev = curr
        curr = curr.next
        
    if curr is not None:
        new_node = Node(val)
        prev.next = new_node
        new_node.next = curr
    return head
    #time complexity = 0(n)
    #space complexity = 0(1)

def delete_at_front(head):
    if head is None:
        return None
    
    curr = head.next
    head = curr
    
    return head
    # or just return head.next
    #time complexity = 0(1)
    #space complexity = 0(1)
    
def delete_at_back(head):
    if head is None:
        return None
    
    if head.next is None:
        return None
    
    curr = head
    while curr.next.next is not None:
        curr = curr.next
    curr.next = None
    return head

    # curr = head
    # prev = None
    # while curr.next is not None:
    #     prev = curr
    #     curr = curr.next
        
    # prev.next = None
    
    # return head
    
    #time complexity = 0(n)
    #space complexity = 0(1)
    
def delete_at_node(head, location):
    curr = head
    if location == 1:
        head = head.next
        return head
    
    prev =  None
    for i in range (1, location):
        prev = curr
        curr = curr.next
        
    prev.next = curr.next
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

def reverseIterative(head):
    prev = None
    curr = head
    
    while curr is not None:
        next_node = curr.next   
        curr.next = prev         
        prev = curr           
        curr = next_node      
    
    return prev
    #time complexity = 0(n)
    #space complexity = 0(1)

def reverseRecursive(head):
    if head is None or head.next is None:
        return head 
    
    new_head = reverseRecursive(head.next)
    
    head.next.next = head
    head.next = None
    
    return new_head
    #time complexity = 0(n)
    #space complexity = 0(n)

def display(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


head = None       

head = insert_at_front(head, 10)
head = insert_at_front(head, 20)
head = insert_at_front(head, 30)
head = insert_at_front(head, 40)
print("Linked List front insertion: ", end="")
display(head)

head = insert_at_end(head, 0)
print("Linked List at end insertion: ", end="")
display(head)

head = insert_after(head, 6, 30)
print("Linked List after insertion: ", end="")
display(head)

head = insert_before(head, 5, 6)
print("Linked List before insertion: ", end="")
display(head)

head = delete_at_front(head)
print("Linked List front deletion: ", end="")
display(head)

head = delete_at_back(head)
print("Linked List end deletion: ", end="")
display(head)

head = delete_at_node(head, 2)
print("Linked List deletion: ", end="")
display(head)

print("Linked List length: ", length(head))

head = reverseIterative(head)
print("Linked List reverse: ", end="")
display(head)

head = reverseRecursive(head)
print("Linked List reverse: ", end="")
display(head)
